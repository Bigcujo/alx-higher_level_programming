#!/usr/bin/python3
""" Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle. """
    number_of_instances = 0
    print_symbol = "#"
    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
        width (int):The width of the new rectangle.
        height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """this will be for getter and setter."""
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
        """this will be for getter and setter for height """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def perimeter(self):
        """Return the perimeter of the Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def area(self):
        """Return the area of the rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """Return the printable represntaion of the Rectangle.
        and it's going to show this with £ charater.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for f in range(self.__height):
            [rect.append(str(self.print_symbol)) for d in range(self.__width)]
            if f != self.height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Return the string represnataion of the rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """this will delete one instance and prints a message after deletion of rectangle"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

