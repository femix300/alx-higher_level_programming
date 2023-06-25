#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0

    previous_value = 0
    total = 0
    dict_of_values = {"I": 1, "V": 5, "X": 10, "L": 50,
                      "C": 100, "D": 500, "M": 1000}
    for char in roman_string:
        if char in dict_of_values:
            value = dict_of_values[char]
            if value <= previous_value:
                total += value
            else:
                total -= 2 * previous_value
                total += value
            previous_value = value
    return total
