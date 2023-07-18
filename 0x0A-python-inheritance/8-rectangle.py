#!/usr/bin/python3
"""
Contains the class Rectangle that inherits from BaseGeometery
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that inherits the class BaseGeometry"""

    def __init__(self, width, height):
        """validate width and height"""
        self.integer_validator("width", width) that inherits from BaseGeometery
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
