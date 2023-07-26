#!/usr/bin/python3
from models.base import base
"""Defines a child class"""


class Rectangle(Base):

    """A rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the rectangle class

        Args:
            width: the width of the rectangle
            height: the rectangles's height
            x: it's x coordinate
            y: it's y coordinate
            id: it's identity

        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """gets the value of the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value for the width"""
        self.__width = value

    @property
    def height(self):
        """gets the value for the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value for the height"""
        self.__height = value

    @property
    def x(self):
        """gets the value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the value of x"""
        self.__x = value

    @property
    def y(self):
        """gets the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the value of y"""
        self.__y = value
