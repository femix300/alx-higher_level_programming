#!/usr/bin/python3
"""Defines a class Square that inherits from a class Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class square that is a granchild to BaseGeometry"""

    def __init__(self, size):
        """creates a private attribute
           Args:
                size(int): the size of the square
           Return:
                The area of the square or raises an exception
        """

        """A class square that is a granchild to BaseGeometry"""

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
