# add path of your project root here so that src is recognised
# python should have the path of this directory (project root) in the PYTHONPATH environment variable
# the error occurs bec the test are run from inside the test directory, where it does not have src inside the test directory

# sorting the problem by adding conftest.py inside test folder and getting project_root in that conftest.py

import os
import sys

# Get the absolute path of the project root directory
# print( os.path.dirname(__file__) )
# print( os.path.join( os.path.dirname(__file__), ".." ) )
# print( os.path.abspath( os.path.join( os.path.dirname(__file__), ".." ) ) )

project_root = os.path.abspath( os.path.join( os.path.dirname(__file__), ".." ) )
sys.path.insert(0, project_root)