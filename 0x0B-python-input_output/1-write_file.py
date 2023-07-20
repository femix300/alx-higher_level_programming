#!/usr/bin/python3

"""Defines a text writing function"""


def write_file(filename="", text=""):
    """a function that writes a string to a text file (UTF8)
    Args:
        filename: the path of the file
        text: the text to be written to the file
    Return:
         the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
