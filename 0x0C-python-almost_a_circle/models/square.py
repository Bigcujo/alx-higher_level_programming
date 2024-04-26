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
    
    @property
    def size(self):
        """
        this will be for the getther method
        """
        return self.height

    @size.setter
    def size(self, value):
        """
        this will be for the setter function
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        this is the sring representaion
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.height)
    
    def update(self, *args, **kwargs):
        """
        this is for the update method
        """
        if args:
            atrributesi = ["id", "size", "x", "y"]
            f = 0
            for f, attrs in enumerate(attributesi):
                if f < len(args):
                    setattr(self, attrs, args[f])
