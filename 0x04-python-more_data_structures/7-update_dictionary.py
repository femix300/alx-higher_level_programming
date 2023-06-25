#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for keys in a_dictionary.keys():
        if keys == key:
            a_dictionary[keys] = value
    if key not in a_dictionary.keys():
        a_dictionary[key] = value
    return a_dictionary
