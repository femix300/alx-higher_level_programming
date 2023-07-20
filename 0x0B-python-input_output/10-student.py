#!/usr/bin/python3

"""Defines a Student class"""


class Student:
    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance
        Args:
            attrs (list of str): A list of attribute names to retrieve.
        Returns:
            dict: A dictionary containing the specified
            attributes and their values.
        """
        if isinstance(attrs, list) and
        all(isinstance(attr, str) for attr in attrs):
            return {attr: getattr(obj, attr) for attr in attrs}
        return self.__dict__
