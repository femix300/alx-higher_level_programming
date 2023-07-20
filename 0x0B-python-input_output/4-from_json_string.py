#!/usr/bin/python3

"""A JSON representation function"""
import json


def from_json_string(my_str):
    """A function that returns an object (Python data structure)
    represented by a JSON string
    Args:
        my_str (str): the json stringto be converted to python object
    """
    return json.loads(my_str)
