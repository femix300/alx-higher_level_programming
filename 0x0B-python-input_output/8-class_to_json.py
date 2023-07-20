#!/usr/bin/python3

"""Defines a JSON serilization/representation function"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure
    for JSON serialization of an object"""
    if isinstance(obj, dict):
        return {key: class_to_json(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [class_to_json(item) for item in obj]
    if hasattr(obj, '__dict__'):
        return {key: class_to_json(value)
                for key, value in obj.__dict__.items()}

    return obj
