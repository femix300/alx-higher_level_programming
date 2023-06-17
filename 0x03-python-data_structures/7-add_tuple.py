#!/usr/bin/python3

def populate_tuple(tuple_x=()):
    if len(tuple_x) < 2:
        if len(tuple_x) == 1:
            tuple_x = (tuple_x[0], 0)
        else:
            tuple_x = (0, 0)
    else:
        tuple_x = (tuple_x[0], tuple_x[1])
    return tuple_x


def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) != 2:
        tuple_a = populate_tuple(tuple_a)
    if len(tuple_b) != 2:
        tuple_b = populate_tuple(tuple_b)

    a, b = tuple_a
    x, y = tuple_b

    _sum = (a + x, b + y)
    return _sum
