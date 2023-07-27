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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation 'json_string' """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                json_string = cls.to_json_string(list_dicts)
                file.write(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename) as file:
                json_data = file.read()
        except FileNotFoundError:
            return []
        dict_list = cls.from_json_string(json_data)
        return [cls.create(**data) for data in dict_list]
