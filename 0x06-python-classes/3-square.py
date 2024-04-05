#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """ This will be for my class named square"""
    def __init__(self, size=0):

    """
    args:
    size (int) : this is for the size of the square.
    """
     
     if not isinstance(size, int):
         raise TypeError("size must be an integer")
     elif size < 0:
         raise ValueError("size must be >= 0")
     else
     self.__size = size

