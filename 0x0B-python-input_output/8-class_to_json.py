#!/usr/bin/python3

"""this function prints out the dictionary descrition of a class"""

def class_to_json(obj):
    """initaialize the function name."""
    return obj.__dict__
