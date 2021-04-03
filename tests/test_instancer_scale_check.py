#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import unittest

from pxr import Sdf, Usd, UsdGeom

from usd_utilities import instancer_scale_check

_SCALAR = 40
_BASIC_INSTANCER_COUNT = 1000


class Run(unittest.TestCase):
    def test_complex(self):
        raise ValueError()

    def test_empty(self):
        stage = Usd.Stage.CreateInMemory()
        self.assertFalse(instancer_scale_check.get_bad_scale_values(stage.TraverseAll()))

    def test_mixed(self):
        stage = Usd.Stage.CreateInMemory()
        bad_values = [
            (0, 0.00000000004001),
            (101, 0.0000000010001),
            (200, 0.0000009000001),
            (5, 0.00000010000001),
        ]
        bad_indices = sorted([index for index, _ in bad_values])
        good_values = [(12, 30), (1020, 30), (3012, 100)]

        instancer = _make_point_instancer(stage, "/foo", issues=bad_values + good_values)

        self.assertEqual(
            [(instancer, bad_indices)],
            instancer_scale_check.get_bad_scale_values(stage.TraverseAll()),
        )

    def test_multiple(self):
        stage = Usd.Stage.CreateInMemory()
        issues_1 = [(5, 0.0000000000001)]
        indices_1 = [index for index, _ in issues_1]
        instancer_1 = _make_point_instancer(stage, "/foo_1", issues=issues_1)
        issues_2 = [
            (5, 0.0000000000001),
            (12, -0.000001),
            (13, -0.000001),
        ]
        indices_2 = [index for index, _ in issues_2]
        instancer_2 = _make_point_instancer(stage, "/foo_2", issues=issues_2)

        self.assertEqual(
            [(instancer_1, indices_1), (instancer_2, indices_2)],
            instancer_scale_check.get_bad_scale_values(stage.TraverseAll()),
        )

    def test_negative(self):
        raise ValueError()

    def test_single(self):
        stage = Usd.Stage.CreateInMemory()
        issues = [(5, 0.0000000000001)]
        indices = [index for index, _ in issues]
        instancer = _make_point_instancer(stage, "/foo", issues=issues)

        self.assertEqual(
            [(instancer, indices)],
            instancer_scale_check.get_bad_scale_values(stage.TraverseAll()),
        )

    def test_zero(self):
        raise ValueError()


def _get_position():
    return (
        (random.random() * _SCALAR) + 0.3,
        (random.random() * _SCALAR) + 0.3,
        (random.random() * _SCALAR) + 0.3,
    )


def _make_bad_value(value=0.00000001):
    indices = list(range(3))
    bad_index = random.choice(indices)

    values = [1 for _ in indices]
    values[bad_index] = value

    return values


def _make_point_instancer(
    stage,
    path,
    issues=0,
    suggested_count=_BASIC_INSTANCER_COUNT,
):
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

        positions = Sdf.AttributeSpec(child, "positions", Sdf.ValueTypeNames.Vector3fArray)
        values = [_get_position() for _ in range(count)]

        for index, value in issues:
            values[index] = _make_bad_value(value=value)

        positions.default = values

    return stage.GetPrimAtPath(path)
