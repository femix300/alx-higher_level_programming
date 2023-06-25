#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for keys, values in sorted(a_dictionary.items()):
        print("{}: {}".format(keys, values))
a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
print_sorted_dictionary(a_dictionary)
