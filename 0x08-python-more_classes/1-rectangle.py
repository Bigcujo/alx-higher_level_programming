#!/usr/bin/python3
"""Define a Rectangle class."""

class Rectangle:
    """this will be for the class Rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width: this will be the width of the rectangle.
            height: this will be the hieght of the rectanglle.

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """this will be the get instance for the rectangle"""
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
        """Get instance of height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
