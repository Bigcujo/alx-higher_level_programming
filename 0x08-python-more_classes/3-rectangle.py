#!/usr/bin/python3
"""Defines a rectanle class."""

class Recatngle:
    """Represent the rectangle."""

    def __init__(self, width=0, height=0):
        """initialize a new rectangle. 

        Args:
            width : The width of the new rectangle.
            height: the height of the new rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """get the width os the rectangle."""
        return self.__width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            rasie ValueError("width must be >= 0")
        self._width =value

    @property
    def height(self):
        """get method for height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle"""
        return (self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return the printable structure of the rectangle

        represents the rectangele with the £ character.
        """

        if self.__width == 0 or self.__height == 0:
            return ("")

        shape = []
        for s in range(self.__height):
            [shape.append('#') for d in range(self.__width)]
            if s != self.__height - 1:
                shape.append("\n")
        return ("".join(shape))

