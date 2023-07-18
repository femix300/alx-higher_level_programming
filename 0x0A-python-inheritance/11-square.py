#!/usr/bin/python3
"""Defines a class Square that inherits from a class Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class square that is a granchild to BaseGeometry"""

    def __init__(self, size):
        """creates a private attribute
           Args:
                size(int): the size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
