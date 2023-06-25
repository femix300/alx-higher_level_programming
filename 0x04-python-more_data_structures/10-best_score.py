#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    first_key = next(iter(a_dictionary))
    highest_score = a_dictionary[first_key]
    for value in a_dictionary.values():
        if int(value) > int(highest_score):
            highest_score = value
    for key, value in a_dictionary.items():
        if value == highest_score:
            return key
