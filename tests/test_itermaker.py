#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Make sure :mod:`usd_utilities.itermaker` works as expected."""

import unittest

from pxr import Sdf
from usd_utilities import itermaker


class IterPrimSpec(unittest.TestCase):
    """Make sure :mod:`usd_utilities.itermaker.iter_prim_specs` works."""

    def test_empty(self):
        """Return only the pseudo-root / root Prim when the Layer is empty."""
        layer = Sdf.Layer.CreateAnonymous()

        self.assertEqual([layer.pseudoRoot], list(itermaker.iter_prim_specs(layer)))
        self.assertEqual(
            [layer.pseudoRoot], list(itermaker.iter_prim_specs(layer.pseudoRoot))
        )

    def test_single(self):
        """Return a single child."""
        raise ValueError()

    def test_multiple(self):
        """Return all children."""
        raise ValueError()

    def test_nested(self):
        """Return nested."""
        raise ValueError()

    def test_performance(self):
        """Make sure the C++ function is faster than Python."""
        raise ValueError()
