#!/usr/bin/python3
for ascii_number in range(97, 123):
    if chr(ascii_number) not in ("q", "e"):
        print("{}".format(chr(ascii_number)), end='')
