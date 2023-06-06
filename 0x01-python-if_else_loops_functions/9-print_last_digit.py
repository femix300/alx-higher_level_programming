#!/usr/bin/python3
def print_last_digit(number):
    if number is None:
        return
    if number < 0:
        last_digit = -(abs(number) % 10)
    else:
        last_digit = number % 10
    if last_digit < 0:
        last_digit = abs(last_digit)
    print("{}".format(last_digit), end='')
    return last_digit
