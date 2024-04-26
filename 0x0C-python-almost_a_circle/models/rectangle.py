#!/usr/bin/python3
"""
Rectanlge module.
"""
from models.base import Base

class Rectangle(Base):
    """
    Rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        """
        initialize the new rectangle.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y


    @property
    def width(self):
        """
        this is the getter method.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        this is the setter method.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value


    @property
    def height(self):
        """
        this is the getter method.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        this is the setter method
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value


    @property
    def x(self):
        """
        this is the getter method
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        this is the setter method
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        this is the getter method
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        this is the setter method.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value


    def area(self):
        """
        this will be for the area of the rectangle.
        """
        area = self.width * self.height
        return area

    def display(self):
        """
        this will be for the display method
        """
        for t in range(self.y):
            print()
        for r in range(self.height):
            print( " " * self.x + "#" * self.width)

    def __str__(self):
        """
        this will be for the string representation of the rectangle.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}". format(self.id, self.x, self.y,self.width, self.height)

    def update(self, *args):
        """
        this will assign values to all the attributes.
        """
        if args:
            attributesi = ["id", "width", "height", "x", "y"]
            f = 0
            for f, attrs in enumerate(attributesi):
                if f < len(args):
                    setattr(self, attrs, args[f])
