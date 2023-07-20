#!/usr/bin/python3

"""Defines a Student class"""


class Student:
    """Retrieves a dictionary representation of a Student instance"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list) and
        all(isinstance(attr, str) for attr in attrs):
            return {attr: getattr(obj, attr) for attr in attrs}
        return self.__dict__
