#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from pxr import Usd

from usd_utilities import instancer_scale_check


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
        indices = [5]
        instancer = _make_point_instancer(stage, "/foo", issues=indices)

        self.assertEqual(
            [(instancer, indices)],
            instancer_scale_check.get_bad_scale_values(stage.TraverseAll()),
        )


def _make_point_instancer(stage, path, issues=0):
    raise ValueError()
