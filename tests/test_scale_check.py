#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Make sure :mod:`usd_utilities.scale_check` works."""

import os
import random
import unittest

from pxr import Sdf, Usd, UsdGeom
from usd_utilities import scale_check

from . import common

_BASE_COUNT = 10000
_BOUND_VALUE = float(os.getenv("USD_CPP_UTILITIES_SCALE_UPPER_BOUND", 0.0001))
_CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
_SCALAR = 40


class Performance(unittest.TestCase):
    """Make sure the C++ implementation works quickly on large sets of data."""

    def test_cpp_is_faster(self):
        """Make sure the C++ implementation is faster than an equivalent Python function."""
        data_path = os.path.join(_CURRENT_DIRECTORY, "big_instancer_data.usdc")
        # Note : The stage below was generated using this code. Uncomment to re-generate it
        # stage = Usd.Stage.CreateInMemory()
        #
        # for instancer_index in range(30):
        #     issues = [(10001, 0.00001), (301, 0.00001)]
        #     _make_point_instancer(
        #         stage,
        #         "/foo_{instancer_index}".format(instancer_index=instancer_index),
        #         issues=issues,
        #         suggested_count=200000,
        #     )
        #
        # stage.GetRootLayer().Export(data_path)

        stage = Usd.Stage.Open(data_path)

        with common.Timer() as python_timer:
            python_results = _get_bad_values(stage.TraverseAll())

        with common.Timer() as cpp_timer:
            cpp_results = _get_cpp_values(stage.TraverseAll())

        self.assertEqual(python_results, cpp_results)

        # The C++ implementation should be at least 250x faster than Python's
        self.assertLess(
            cpp_timer.get_recorded_delta() * 250, python_timer.get_recorded_delta(),
        )


class Run(unittest.TestCase):
    """Make sure :func:`usd_utilities.scale_check.get_bad_scale_values` works."""

    def test_empty(self):
        """Make sure an empty USD stage / range can be processed."""
        stage = Usd.Stage.CreateInMemory()
        self.assertFalse(_get_cpp_values(stage.TraverseAll()))

    def test_mixed(self):
        """Report only the bad values in a mixture of explicit good / bad values."""
        stage = Usd.Stage.CreateInMemory()
        bad_values = [
            (0, 0.00000000004001),
            (101, 0.0000000010001),
            (200, 0.0000009000001),
            (5, 0.00000010000001),
        ]
        bad_indices = sorted([index for index, _ in bad_values])
        good_values = [(12, 30), (1020, 30), (3012, 100)]

        attribute = _make_point_instancer(
            stage, "/foo", issues=bad_values + good_values
        )

        self.assertEqual(
            [(attribute, bad_indices)], _get_cpp_values(stage.TraverseAll()),
        )

    def test_multiple(self):
        """Test multiple PointInstancers at once."""
        stage = Usd.Stage.CreateInMemory()
        issues_1 = [(5, 0.0000000000001)]
        indices_1 = [index for index, _ in issues_1]
        attribute_1 = _make_point_instancer(stage, "/foo_1", issues=issues_1)
        issues_2 = [
            (5, 0.0000000000001),
            (12, -0.000001),
            (13, -0.000001),
        ]
        indices_2 = [index for index, _ in issues_2]
        attribute_2 = _make_point_instancer(stage, "/foo_2", issues=issues_2)

        self.assertEqual(
            [(attribute_1, indices_1), (attribute_2, indices_2)],
            _get_cpp_values(stage.TraverseAll()),
        )

    def test_negative(self):
        """Make sure negative, small values are caught."""
        stage = Usd.Stage.CreateInMemory()
        issues = [(5, -0.0000000000001)]
        indices = [index for index, _ in issues]
        attribute = _make_point_instancer(stage, "/foo", issues=issues)

        self.assertEqual(
            [(attribute, indices)], _get_cpp_values(stage.TraverseAll()),
        )

    def test_single(self):
        """Catch a single bad, small value."""
        stage = Usd.Stage.CreateInMemory()
        issues = [(5, 0.0000000000001)]
        indices = [index for index, _ in issues]
        attribute = _make_point_instancer(stage, "/foo", issues=issues)

        self.assertEqual(
            [(attribute, indices)], _get_cpp_values(stage.TraverseAll()),
        )

    def test_zero(self):
        """Make sure 0 values are caught."""
        stage = Usd.Stage.CreateInMemory()
        issues = [(5, 0)]
        indices = [index for index, _ in issues]
        attribute = _make_point_instancer(stage, "/foo", issues=issues)

        self.assertEqual(
            [(attribute, indices)], _get_cpp_values(stage.TraverseAll()),
        )


def _get_bad_values(prims):
    """Find all scale values which are too small.

    This function is a Python-equivalent of the C++
    :func:`usd_utilities.scale_check.get_bad_scale_values` function.

    Args:
        prims (iter[:class:`pxr.Usd.Prim`]):
            Each Prim to consider. Non Point Instancers will be ignored.

    Returns:
        set[tuple[:class:`pxr.Usd.Attribute`, list[int]]]:
            Each Attribute which has bad scale values and the found indices.

    """

    def _is_too_low(value):
        return abs(value) < _BOUND_VALUE

    bads = []

    for prim in prims:
        instancer = UsdGeom.PointInstancer(prim)

        if not instancer:
            continue

        attribute = instancer.GetScalesAttr()
        indices = []

        for index, value in enumerate(attribute.Get()):
            if _is_too_low(value[0]) or _is_too_low(value[1]) or _is_too_low(value[2]):
                indices.append(index)

        if indices:
            bads.append((instancer.GetScalesAttr(), indices))

    return bads


def _get_cpp_values(prims):
    output = []

    for prim in prims:
        instancer = UsdGeom.PointInstancer(prim)

        if not instancer:
            continue

        attribute = instancer.GetScalesAttr()
        indices = scale_check.get_bad_scale_values(attribute)

        if indices:
            output.append((attribute, indices))

    return output


def _get_scale():
    """tuple[float, float, float]: Create a valid, 3-tuple for testing."""
    return (
        (random.random() * _SCALAR) + 0.3,
        (random.random() * _SCALAR) + 0.3,
        (random.random() * _SCALAR) + 0.3,
    )


def _make_value(value):
    """Make a 3-tuple with a value at as one of its components.

    The chosen component (0th, 1st, or 2nd) is chosen randomly.

    Args:
        value (float): A value to add to one of the components.

    Returns:
        tuple[float, float, float]: The generated 3-tuple.

    """
    indices = list(range(3))
    bad_index = random.choice(indices)

    values = [1 for _ in indices]
    values[bad_index] = value

    return values


def _make_point_instancer(  # pylint: disable=too-many-locals,bad-continuation
    stage, path, issues=tuple(), suggested_count=_BASE_COUNT,
):
    """Create a PointInstancer for testing.

    Args:
        stage (:class:`pxr.Usd.Stage`):
            A USD object to add this new PointInstancer to.
        path (str):
            The absolute USD namespace where the new PointInstancer will go.
        issues (list[container[int, int or float]], optional):
            Each index and value which set directly onto the newly
            created PointInstancer's scale attribute. Use this parameter
            for testing good and bad values.
        suggested_count (int, optional):
            The number of instances which will be created, at
            minimum. Default: 10000.

    Returns:
        :class:`pxr.Usd.Attribute`:
            The generated PointInstancer attribute to test for.

    """
    layer = stage.GetRootLayer()
    count = max(max([index for index, _ in issues]) + 1, suggested_count)

    with Sdf.ChangeBlock():
        mesh = Sdf.CreatePrimInLayer(layer, "/sphere")
        mesh.specifier = Sdf.SpecifierDef
        mesh.typeName = UsdGeom.Sphere.__name__

        child = Sdf.CreatePrimInLayer(layer, path)
        child.specifier = Sdf.SpecifierDef
        child.typeName = UsdGeom.PointInstancer.__name__
        indices = Sdf.AttributeSpec(child, "protoIndices", Sdf.ValueTypeNames.IntArray)
        indices.default = [0 for _ in range(count)]

        prototypes = Sdf.RelationshipSpec(child, "prototypes", custom=False)
        prototypes.targetPathList.explicitItems.append(mesh.path)

        scales = Sdf.AttributeSpec(child, "scales", Sdf.ValueTypeNames.Vector3fArray)
        values = [_get_scale() for _ in range(count)]

        for index, value in issues:
            values[index] = _make_value(value)

        scales.default = values

    prim = stage.GetPrimAtPath(path)

    return UsdGeom.PointInstancer(prim).GetScalesAttr()


def _yield_elements(container):
    """Re-yield every element within `container`."""
    for element in container:
        yield element
