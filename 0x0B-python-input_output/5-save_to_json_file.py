#!/usr/bin/python3
"""Defines a a function that writes json string to a file"""
import json

def save_to_json_file(my_obj, filename):
    """write an object to a text file using json representation."""
    with open(filename, mode="w") as f:
        json.dump(my_obj, f)
