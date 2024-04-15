#!/usr/bin/pyhton3
""" Class for Rectangle which is a sub class of BaseGeometry."""

class BaseGeometry:
    def area(self):
        '''Raises Exception error with the message "area() is not implemented".'''
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        ''' this validates the integer to be either an integer or greater than 0
.'''
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        if not isinstance(value, int):
            raise TypeError("{} must be an integer")

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.__height = 0
        self.__width = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.width = width
        self.__height = height
