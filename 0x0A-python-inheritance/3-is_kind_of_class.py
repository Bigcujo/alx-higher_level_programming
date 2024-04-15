#!/usr/bin/python3
'''Module for is_kind_of_class method.'''


def is_kind_of_class(obj, a_class):
    '''this function checks if the object is the same instance of the class or instance of the sub class'''
    return isinstance(obj, a_class)
