#!/usr/bin/python3
"""Define a class Square. """


class Square:
    """ Represent a square."""

    def __init__(self, size):
        """this is the construtor

        Args:
            size (int): The size of the new square.

            """
        self.size = size

    @property
    def size(self):
       """ this will get the current value of square"""
       return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value 
         
    def area(self):
        """ return the area of the current square."""
        return (self.__size ** 2)

    def my_print(self):
        """ print the number of square with #"""

        for j in range(0, self.__size):
            [print("#", end="") for f in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
