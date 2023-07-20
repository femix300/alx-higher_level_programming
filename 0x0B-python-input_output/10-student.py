#!/usr/bin/python3

"""Defines a Student Class"""


class Student:
    """
    Represents a student.

    Args:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs):
        """
        Retrieves a dictionary representation of the Student instance.

        Args:
            attrs (list of str): List of attribute names to retrieve.

        Returns:
            dict: Dictionary containing the specified
            attributes and their values.

        If 'attrs' list is empty, it returns a dictionary representation
        of all attributes of the Student instance.
        """
        if isinstance(attrs, list) and
        all(isinstance(attr, str) for attr in attrs):
            return {attr: getattr(self, attr) for attr in attrs}
        return self.__dict__
