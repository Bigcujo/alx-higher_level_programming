#!/usr/bin/python3
""" Module for BaseGeometry class."""

class BaseGeometry:
    def area(self):
        '''Raises Exception error with the message "area() is not implemented".'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        ''' this validates the integer to be either an integer or greater than 0.'''
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
