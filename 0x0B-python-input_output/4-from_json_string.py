#!/usr/bin/python3
"""define a json-to-object function."""
import json

def from_json_string(my_str):
    """Return the python object value of a json string."""
    return json.loads(my_str)
