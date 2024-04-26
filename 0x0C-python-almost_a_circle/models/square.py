#!/usr/bin/python3
"""
Square module.
"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """
    this will be for the square class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Square class constructor.
        """
        super().__init__(size, size, x, y, id)
    
    def __str__(self):
        """
        this is the sring representaion
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.height)

