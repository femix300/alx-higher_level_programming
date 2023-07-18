#!/usr/bin/python3

"""defines a class checking function"""


def is_kind_of_class(obj, a_class):
    """Checks if  object is an instance of, or if the object
    is an instance of a class that inherited from,
    the specified class

    Args:
        obj (any): the object
        a_class (object): the specified class
    Returns:
        True: if the objeect is an instance or a subclass of the
              specified class
        False: if otherwise
    """
    return isinstance(obj, a_class) or issubclass(type(obj), a_class)
