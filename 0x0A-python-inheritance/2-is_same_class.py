#!/usr/bin/python3
'''Module for is_same_class method.'''


def is_same_class(obj, a_class):
    '''Check if the object is exactly an instance of the specified class.'''
    return isinstance(obj, a_class) and type(obj) == a_class
