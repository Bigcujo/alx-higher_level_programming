#!/usr/bin/python3
"""Defining a rectangle class."""

class Rectangle:
    """Representing a rectangle."""

    def __init__(self, width=0, height=0):
        """Initaialize a new Rectangle class.

        Args:
        width: The width os the rectangle.
        height:the height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the  rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get the value for the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value


    def area(self):
        """this will return the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """this will return the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
