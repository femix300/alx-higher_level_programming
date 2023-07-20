#!/usr/bin/python3

"""A text-file appending function"""


def append_write(filename="", text=""):
    """a function that appends a string at the end of a text file (UTF8)
    Args:
        filename: the path of the file
        text: the text to be appended to the file
    Return:
        The number of characters added
    """
    with open(filename, "a", encoding='utf-8') as file:
        return file.write(text)
