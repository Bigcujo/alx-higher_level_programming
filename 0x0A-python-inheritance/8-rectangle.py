#!/usr/bin/pyhton3
""" Class for Rectangle which is a sub class of BaseGeometry."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.__height = 0
        self.__width = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
