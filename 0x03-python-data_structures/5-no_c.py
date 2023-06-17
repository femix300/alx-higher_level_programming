#!/usr/bin/python3
def no_c(my_string):
    if not my_string:
        return my_string
    new_str = []
    for char in my_string:
        if char != 'c' and char != 'C':
            new_str.append(char)
    new_str = ''.join(new_str)
    return new_str
