#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    check_items = []
    for item in my_list:
        if item in check_items:
            continue
        else:
            check_items.append(item)
            result += int(item)
    return result
