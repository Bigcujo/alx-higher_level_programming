#!/usr/bin/python3
"""To define the rectangle class."""

class Rectangle:
    """Represent the rectangle."""

    def __init__(self, width=0, height=0):
        """Iniialzie the rectangle so it can take in varables or argument

        args:

            width (int): the width of the new rectangle.
            height(int): the height of the new rectangle.

            """

    @property
    def width(self):
                """this will be the get and set of the rectangle"""
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
        """get and set for height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """this will return the area of the rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        if self.__width == 0 or self.height == 0:
            return (0)
        return ((self.width * 2) + (self.height * 2))

    def __str__(self):
        """retuns the the visible part of the rectangle.

        and it will represt it with the # charater."""

        if self.__width == 0 or self.height == 0:
            return ("")

        rect = []
        for j in range(self.height):
            [rect.append('#') for d in range(self._width)]
            if j != self._height - 1:
                rect.append("\n")
        return ("".join(rect))


