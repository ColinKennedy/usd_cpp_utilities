#!/usr/bin/env python
# -*- coding: utf-8 -*-

name = "usd_cpp_utilities"

version = "1.0.0"

description = "Miscellaneous, optimized functions for working with USD"

authors = ["ColinKennedy"]

private_build_requires = ["cmake-3"]

# TODO : Can this be private / build requires?
requires = ["USD-20.02.4+<21", "~python-2.7"]

tests = {
    "black_diff": {
        "command": "rez-env black-19 -- black --diff --check tests",
    },
    "black": {
        "command": "rez-env black-19 -- black tests",
        "run_on": "explicit",
    },
    "build_documentation": {
        "command": "doxygen",
        # "requires": ["doxygen"],  # TODO : Add a Rez package for this, later
        "run_on": "explicit",
    },
    "isort": {
        "command": "isort --recursive tests",
        "requires": ["isort-4.3+<5"],
        "run_on": "explicit",
    },
    "isort_check": {
        "command": "isort --check-only --diff --recursive tests",
        "requires": ["isort-4.3+<5"],
    },
    "pydocstyle": {
        # Need to disable D202 for now, until a new pydocstyle version is released
        # Reference: https://github.com/psf/black/issues/1159
        #
        "command": "pydocstyle --ignore=D213,D202,D203,D406,D407 tests/*",
        "requires": ["pydocstyle-3+<4"],
    },
    "pylint": {"command": "pylint tests", "requires": ["pylint-1.9+<2"]},
    "unittest": "python -m unittest discover",
}


def commands():
    import os

    # TODO : Check that these values are required
    env.CMAKE_MODULE_PATH.append(os.path.join(root, "cmake"))
    env.CPP_INCLUDE_PATH.append(os.path.join(root, "include"))
    env.LD_LIBRARY_PATH.append(os.path.join(root, "lib"))
    env.LIBRARY_PATH.append(os.path.join(root, "lib"))
    env.PYTHONPATH.append(os.path.join(root, "lib", "python"))
