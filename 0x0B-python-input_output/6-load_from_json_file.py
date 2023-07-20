#!/usr/bin/python3

"""Defines a JSON object creating function"""
import json


def load_from_json_file(filename):
    """A function that creates an Object from a 'JSON file'"""
    with open(filename) as file:
        return json.load(file)
