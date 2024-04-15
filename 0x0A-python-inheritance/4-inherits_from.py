#!/usr/bin/python3
'''Module for is_kind_of_class method.'''


def inherits_from(obj, a_class):
    '''Check if the object is an instance of a class inherited (directly or indirectly) from the specified class.'''
    return isinstance(obj, object) and issubclass(type(obj), a_class) and type(obj) != a_class

