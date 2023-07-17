#!/usr/bin/python3

"""Defines a class that inherits from list"""


class MyList(list):
    """a derived class from list"""

    def __init__(self):
        super().__init__(self)

    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
