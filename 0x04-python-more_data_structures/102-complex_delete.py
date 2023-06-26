#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_of_keys = []
    if value not in a_dictionary.values():
        return a_dictionary
    for key, the_value in a_dictionary.items():
        if the_value == value:
            list_of_keys.append(key)
    for key in list_of_keys:
        del a_dictionary[key]

    return a_dictionary
