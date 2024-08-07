#!/usr/bin/python3

"""State a class Square"""

class Square:
    """this be for the square."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
        size (int) : the size of the new square.

        """
        self.size = size

    @property

    def size(self):
            """ Get the current size of the square"""
            return (self.__size)

    @size.setter
    
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError ("size must be an integer")
        elif value < 0:
            raise ValueError ("size must be >= 0")

        self.__size = value

    def area(self):
        """ Return the area of the square"""
        return (self.__size ** 2)
