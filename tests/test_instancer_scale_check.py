#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import unittest

from pxr import Sdf, Usd, UsdGeom

from usd_utilities import instancer_scale_check

_SCALAR = 40
_VALUES = 10


# TODO : Add these tests
# - Negative
# - Small value
# - Zero
#
class Run(unittest.TestCase):
    def test_complex(self):
        raise ValueError()

    def test_empty(self):
        stage = Usd.Stage.CreateInMemory()
        self.assertFalse(instancer_scale_check.get_bad_scale_values(stage.TraverseAll()))

    def test_multiple(self):
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


def _make_point_instancer(stage, path, issues=0):
    layer = stage.GetRootLayer()

    with Sdf.ChangeBlock():
        mesh = Sdf.CreatePrimInLayer(layer, "/sphere")
        mesh.specifier = Sdf.SpecifierDef
        mesh.typeName = UsdGeom.Sphere.__name__

        child = Sdf.CreatePrimInLayer(layer, path)
        child.specifier = Sdf.SpecifierDef
        child.typeName = UsdGeom.PointInstancer.__name__
        indices = Sdf.AttributeSpec(child, "protoIndices", Sdf.ValueTypeNames.IntArray)
        indices.default = [0 for _ in range(_VALUES)]

        prototypes = Sdf.RelationshipSpec(child, "prototypes", custom=False)
        prototypes.targetPathList.explicitItems.append(mesh.path)

        positions = Sdf.AttributeSpec(child, "positions", Sdf.ValueTypeNames.Vector3fArray)
        values = [_get_position() for _ in range(_VALUES)]

        for index, value in issues:
            values[index] = _make_bad_value(value=value)

        positions.default = values

    return stage.GetPrimAtPath(path)
