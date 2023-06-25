#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    mod_dict = dict(a_dictionary)
    for keys, value in mod_dict.items():
        mod_dict[keys] = value * 2
    return mod_dict
