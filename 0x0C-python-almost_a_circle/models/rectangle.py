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
        self.__y = value
