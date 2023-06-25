#!/usr/bin/python3
def search_replace(my_list, search, replace):
    mod_list = []
    for item in my_list:
        if item == search:
            mod_list.append(replace)
        else:
            mod_list.append(item)
    return mod_list
