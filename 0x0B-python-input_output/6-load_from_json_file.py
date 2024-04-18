#!/usr/bin/python3
"""Defines a json file reading function."""
import json

def load_from_json_file(filename):
    """create a python object from a json file."""
    with open(filename) as files:
        return json.load(files)
