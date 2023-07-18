#!/usr/bin/python3
"""
Defines the class BaseGeometry
"""


class BaseGeometry:
    """A class that contains area and integer_validator methods"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
