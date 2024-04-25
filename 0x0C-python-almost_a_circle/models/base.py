#!/usr/bin/python3
""" 
this defines the base model calss
"""


class Base:
    """
    this will represent the base class.
    """
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
