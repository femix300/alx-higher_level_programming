#!/usr/bin/python3
def remove_char_at(str, n):
    if str is None or n is None:
        return
    if n >= len(str) or n < 0:
        return str

    mod_str = ""
    for character in str:
        if character != str[n]:
            mod_str += character
    return mod_str
