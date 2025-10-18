"""
=========================================================================================
CONFIGURATION FILE: conftest.py
-----------------------------------------------------------------------------------------
PURPOSE:
    Ensures that the test suite can properly locate and import the project's source modules
    (e.g., `backend`, `db_helper`, etc.) when tests are executed from within the `tests/`
    directory.

WHY THIS IS NEEDED:
    - By default, when pytest runs inside the `tests/` folder, Python’s import system
      does not automatically include the parent (project root) directory in sys.path.
    - As a result, imports like `from backend import db_helper` or similar may fail.
    - This file fixes that by dynamically adding the project root path to sys.path.

USAGE:
    Simply keep this file inside the `tests/` directory.
    Pytest automatically detects and loads it during test execution.

EXAMPLE RUN:
        pytest

EFFECT:
    This ensures that all project modules (inside src/backend/, etc.) can be imported
    directly without causing `ModuleNotFoundError`.

AUTHOR:
    (Your Name)
=========================================================================================
"""

import os
import sys


# --------------------------------------------------------------------------------------
# Determine the absolute path to the project root directory.
# __file__                  --> path of this conftest.py file (inside /tests).
# os.path.dirname(__file__) --> gives the /tests directory path.
# os.path.join(..., "..")   --> moves one level up to reach the project root.
# os.path.abspath(...)      --> converts it into an absolute path string.
# --------------------------------------------------------------------------------------
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


# --------------------------------------------------------------------------------------
# Insert the project root at the beginning of sys.path.
# This ensures Python looks here first when resolving imports.
# Without this, pytest may not recognize imports like `from backend import db_helper`.
# --------------------------------------------------------------------------------------
sys.path.insert(0, project_root)
