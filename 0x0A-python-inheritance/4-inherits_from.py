#!.usr.bin.python3
"""Defines a class checking function"""


def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class.

    Args:
        obj (any): the object
        a_class (object): the specified class

    Returns:
        True: if the object is an instance of a class
        that inherited from the specified class
        False: if otherwise
    """

    if issubclass(type(obj), a_class) and not type(obj) is a_class:
        return True
    return False
