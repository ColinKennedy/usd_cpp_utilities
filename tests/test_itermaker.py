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
        layer = Sdf.Layer.CreateAnonymous(".usda")
        Sdf.CreatePrimInLayer(layer, "/root/another")
        raise ValueError(list(_iter_from_layer(layer)))

    def test_multiple(self):
        """Return all children."""
        raise ValueError()

    def test_nested(self):
        """Return nested."""
        raise ValueError()

    def test_performance(self):
        """Make sure the C++ function is faster than Python."""
        raise ValueError()

    def test_variants(self):
        layer = Sdf.Layer.CreateAnonymous(".usda")
        layer.ImportFromString(
            """\
            #usda 1.0

            def "root"
            {
                variantSet "thing" = {
                    "one" {
                        def "variant_child"
                        {
                            def "variant_grand_child_1"
                            {
                            }

                            def "variant_grand_child_2"
                            {
                            }
                        }

                        def "foo"
                        {
                        }
                    }
                }

                def "child"
                {
                    def "grand_child_1"
                    {
                    }

                    def "grand_child_2"
                    {
                    }
                }
            }
            """
        )

        results = list(_iter_from_layer(layer))

        self.assertEqual(
            [
                layer.GetPrimAtPath("/"),
                layer.GetPrimAtPath("/root{thing=one}"),
                layer.GetPrimAtPath("/root{thing=one}variant_child"),
                layer.GetPrimAtPath("/root{thing=one}variant_child/variant_grand_child_1"),
                layer.GetPrimAtPath("/root{thing=one}variant_child/variant_grand_child_2"),
                layer.GetPrimAtPath("/root{thing=one}foo"),
                layer.GetPrimAtPath("/root"),
                layer.GetPrimAtPath("/root/child"),
                layer.GetPrimAtPath("/root/child/grand_child_1"),
                layer.GetPrimAtPath("/root/child/grand_child_2"),
            ],
            results,
        )

        raise ValueError(results)


def _iter_prim_spec(root):
    yield root

    for prim_spec in root.nameChildren:
        for variant_set in prim_spec.variantSets:
            for variant_spec in variant_set.variants.values():
                for inner in _iter_prim_spec(variant_spec.primSpec):
                    yield inner

        for child in _iter_prim_spec(prim_spec):
            yield child


def _iter_from_layer(layer):
    for prim_spec in _iter_prim_spec(layer.pseudoRoot):
        yield prim_spec
