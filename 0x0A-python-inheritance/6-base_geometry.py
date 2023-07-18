#!/usr/bin/python3

"""Defines an empty base class"""


class BaseGeometry:
    """A class BaseGeometry that raises an exception"""

    def area(self):
        raise Exception("area() is not implemented")
