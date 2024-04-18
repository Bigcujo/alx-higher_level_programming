#!/usr/bin/python3
"""Define a jason-to-object function."""
import json

def to_json_string(my_obj):
    """Return the json value of a string"""
    return json.dumps(my_obj)
