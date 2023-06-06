#!/usr/bin/python3
def uppercase(str):
    if str is None:
        return
    for character in str:
        letter = ord(character)
        if 97 <= letter <= 122:
            letter -= 32
            character = chr(letter)
        print("{}".format(character), end='')
    print()
