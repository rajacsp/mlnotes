

import os
import sys

def get_myenv():
    return os.environ.get('CONDA_DEFAULT_ENV')

def get_pyv():
    return sys.version

def get_local_pyinfo():

    return f"conda env: {os.environ.get('CONDA_DEFAULT_ENV')}; pyv: {sys.version}"

import importlib.metadata

def get_installed_version(lib_name):
    try:
        version = importlib.metadata.version(lib_name)
        return f"{lib_name}=={version}"
    except importlib.metadata.PackageNotFoundError:
        return f"{lib_name} is not installed in the current environment."
    except Exception as e:
        return f"An error occurred: {e}"

def ps2(lib_names):
    lib_list = lib_names.split()
    results = """"""
    for lib_name in lib_list:
        version = get_installed_version(lib_name)
        results += f"{version}\n"
    return results

def separate_index(line):

    if ". " in line:
        number, text = line.split(". ", 1)  # Split by the first occurrence of ". "
    else:
        number, text = None, line

    return number, text