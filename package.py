#!/usr/bin/env python
# -*- coding: utf-8 -*-

name = "usd_cpp_utilities"

version = "1.0.0"

description = "Miscellaneous, optimized functions for working with USD"

authors = ["ColinKennedy"]

private_build_requires = ["cmake-3"]

# TODO : Can this be private / build requires?
requires = [
    "USD-20.02.4+<21",
    "~python-2.7",
]


def commands():
    import os

    # TODO : Check that these values are required
    env.CMAKE_MODULE_PATH.append(os.path.join(root, "cmake"))
    env.CPP_INCLUDE_PATH.append(os.path.join(root, "include"))
    env.LD_LIBRARY_PATH.append(os.path.join(root, "lib"))
    env.LIBRARY_PATH.append(os.path.join(root, "lib"))
    env.PYTHONPATH.append(os.path.join(root, "lib"))
