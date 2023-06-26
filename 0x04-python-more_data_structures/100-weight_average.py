#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    total = 0
    total_weight = 0
    for tupple in my_list:
        total += tupple[0] * tupple[1]
        total_weight += tupple[1]

    result = total / total_weight
    return result
