

import os
import sys

def get_myenv():
    return os.environ.get('CONDA_DEFAULT_ENV')

def get_pyv():
    return sys.version

def get_local_pyinfo():

    return f"conda env: {os.environ.get('CONDA_DEFAULT_ENV')}; pyv: {sys.version}"