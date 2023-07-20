#!/usr/bin/python3

"""Defines a JSON serilization/representation function"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure
    fon JSON serialization of an object"""
    return obj.__dict__
