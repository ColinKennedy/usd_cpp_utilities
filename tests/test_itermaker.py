#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Make sure :mod:`usd_utilities.itermaker` works as expected."""

import contextlib
import unittest
import time

from pxr import Sdf
from usd_utilities import itermaker


class IterPrimSpecs(unittest.TestCase):
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
        prim_spec = Sdf.CreatePrimInLayer(layer, "/root")
        self.assertEqual(
            [layer.pseudoRoot, prim_spec],
            list(itermaker.iter_prim_specs(layer.pseudoRoot)),
        )

    def test_multiple(self):
        """Return all children."""
        layer = Sdf.Layer.CreateAnonymous(".usda")
        prim_spec_1 = Sdf.CreatePrimInLayer(layer, "/root")
        prim_spec_2 = Sdf.CreatePrimInLayer(layer, "/root/thing")
        prim_spec_3 = Sdf.CreatePrimInLayer(layer, "/root/last")
        self.assertEqual(
            [
                layer.pseudoRoot,
                prim_spec_1,
                prim_spec_2,
                prim_spec_3,
            ],
            list(itermaker.iter_prim_specs(layer.pseudoRoot)),
        )

    def test_performance(self):
        """Make sure the C++ function is faster than Python."""
        layer = _get_big_layer()

        with _time_it() as cpp:
            list(itermaker.iter_prim_specs(layer))

        with _time_it() as python:
            list(_iter_from_layer(layer))

        self.assertTrue(cpp.get_delta() * 10 < python.get_delta())

    def test_variants(self):
        """Get all Layer contents recursively, including variant content."""
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
                layer.GetPrimAtPath(
                    "/root{thing=one}variant_child/variant_grand_child_1"
                ),
                layer.GetPrimAtPath(
                    "/root{thing=one}variant_child/variant_grand_child_2"
                ),
                layer.GetPrimAtPath("/root{thing=one}foo"),
                layer.GetPrimAtPath("/root"),
                layer.GetPrimAtPath("/root/child"),
                layer.GetPrimAtPath("/root/child/grand_child_1"),
                layer.GetPrimAtPath("/root/child/grand_child_2"),
            ],
            results,
        )

        self.assertEqual(results, list(itermaker.iter_prim_specs(layer)))


def _iter_prim_spec(root):
    """Get every PrimSpec on and under `root`.

    This function is inclusive. The first yielded value will be `root`.

    Args:
        root (:class:`pxr.Sdf.PrimSpec`): The PrimSpec to find children from.

    Yields:
        :class:`pxr.Sdf.PrimSpec`: `root` + all of its children, if any.

    """
    yield root

    for prim_spec in root.nameChildren:
        for variant_set in prim_spec.variantSets:
            for variant_spec in variant_set.variants.values():
                for inner in _iter_prim_spec(variant_spec.primSpec):
                    yield inner

        for child in _iter_prim_spec(prim_spec):
            yield child


def _iter_from_layer(layer):
    """Get every PrimSpec on and under some Sdf Layer.

    This function is inclusive. The pseudo-root of `layer` is the first
    PrimSpec yielded.

    Args:
        root (:class:`pxr.Sdf.Layer`): The Layer to get all content of.

    Yields:
        :class:`pxr.Sdf.PrimSpec`: `root` + all of its children, if any.

    """
    for prim_spec in _iter_prim_spec(layer.pseudoRoot):
        yield prim_spec


def _get_big_layer():
    """:class:`pxr.Sdf.Layer`: A USD object with lots of content."""
    layer = Sdf.Layer.CreateAnonymous(".usda")

    with Sdf.ChangeBlock():
        for index in range(10000):
            parent = "/foo_{index}".format(index=index)
            Sdf.CreatePrimInLayer(layer, parent)

            for inner in range(20):
                Sdf.CreatePrimInLayer(layer, parent + "/child_{inner}".format(inner=inner))

    return layer


@contextlib.contextmanager
def _time_it():
    """Time the execution of the code which runs in this context."""
    class Timer(object):
        def __init__(self, start):
            super(Timer, self).__init__()

            self.start = start
            self.end = None

        def get_delta(self):
            if self.end is None:
                raise RuntimeError("No delta can be found.")

            return self.end - self.start

    timer = Timer(time.time())

    try:
        yield timer
    finally:
        timer.end = time.time()
