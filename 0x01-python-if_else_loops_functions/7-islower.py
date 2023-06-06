#!/usr/bin/python3
def islower(c):
    if c is None:
        return
    letter = ord(c)
    if 97 <= letter <= 122:
        return True
    else:
        return False
