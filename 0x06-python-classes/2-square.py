#!/usr/bin/python3

"""Define a class named square."""


class Square:
    """this is for the class name"""

    def __init__(self, size=0):
        """ this is to initialize a new square.

        Args:
        hte size must be an int.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size muust be >= 0")
        else:
            self.__size = size
