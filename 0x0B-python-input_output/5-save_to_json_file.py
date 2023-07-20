#!/usr/bin/python3

"""Defines a JSON representation function"""


def save_to_json_file(my_obj, filename):
    """A function that writes an Object to a text file,
    using a JSON representation
    Args:
        filename (str): The path of the file to be written.
        obj (Any): The Python object to be written to the file.
    """
    with open(filename, "w") as file:
        json.dump(obj, file)
