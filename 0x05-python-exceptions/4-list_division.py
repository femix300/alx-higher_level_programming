#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    try:
        new_list = [x / y for x, y in zip(my_list_1, my_list_2)]
    except TypeError:
        raise ValueError("wrong type")
    except ZeroDivisionError:
        raise ValueError("division by 0")
    except IndexError:
        raise ValueError("out of range")
    else:
        new_list += [0] * (list_length - len(new_list))
    return new_list
