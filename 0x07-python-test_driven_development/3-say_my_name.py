#!/usr/bin/python3


"""
This is the "3-say_my-name" module.
The 3-say_my_name  module supplies one function, say_my_name.
"""


def say_my_name(first_name, last_name=""):
    """
    A function that prints "My name is <first name> <last name>"

    Args:
        first_name: (string)
        last_name: (string)

    Raises:
        TypeError: if first_name and last_name are not strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
