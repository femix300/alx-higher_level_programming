#!/usr/bin/python3
"""Defines a base class"""

import json


class Base:

    """A base class for all other classes

    Private class attribute:
        __nb_objects (int): Number of bases instantiated
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a new base.

        Args:
            self.id (int): the identity of the new base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
