#!/usr/bin/python3

"""A function that checks if an object is an instance
of a specified class"""


def is_same_class(obj, a_class):
    """ if the object is exactly an instance
    of the specified class

    Args:
        obj (any): the objexct to be cheked
        a_class (type): the class that is being cheked for

    Returns:
        True: if the object is an instance of the class
        False: otherwise"""
    return type(obj) is a_class
