#!/usr/bin/python3
"""
This is the "4-print_square" module.
The 4-print_square  module supplies one function, print_square.
"""


def print_square(size):

    """A function that prints a square with the character #

    Args:
        size (int): The the size length of the square to be printed

    Raises:
        A TypeError if size is not an integer
        A ValueError if size is less than 0
        A TypeError if size is a float less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(0, size):
        print("#" * size, end='')
        print()
