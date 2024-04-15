#!/usr/bin/python3
'''Module for lookup method.'''


def lookup(obj):
    '''This function Looks up object attributes and methods in the class given.
    Args:
        obj (object): the object we want to list.

    Returns:
        list: it returns the lists and methods in the class
    '''
    return dir(obj)
