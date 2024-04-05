#!/usr/bin/python3

"""Define a class Square."""

class Square:
    """This class represents a square.

    Attributes:
        __size (int): The size of each side of the square.
    """

    def __init__(self, size=0):
        """Initialize the Square object with a given size.

        Args:
            size (int): The size of each side of the square. Defaults to 0.
        
        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is negative.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

