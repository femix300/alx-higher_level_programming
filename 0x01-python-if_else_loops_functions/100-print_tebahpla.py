#!/usr/bin/python3
for ascii_number in range(122, 96, -1):
    if ascii_number % 2 != 0:
        ascii_number -= 32
    print("{}".format(chr(ascii_number)), end='')
