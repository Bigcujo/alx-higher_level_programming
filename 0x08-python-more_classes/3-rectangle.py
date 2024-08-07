#!/usr/bin/python3
"""Defines a rectangle class."""

class Rectangle:
    """Represent the rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle. 

        Args:
            width : The width of the new rectangle.
            height: The height of the new rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle."""
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
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return the printable structure of the rectangle.

        Represents the rectangle with the '#' character.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        shape = []
        for s in range(self.__height):
            [shape.append('#') for d in range(self.__width)]
            if s != self.__height - 1:
                shape.append("\n")
        return "".join(shape)

