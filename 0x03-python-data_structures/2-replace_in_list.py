#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    idxx = str(element)
    if (idx >= 0) and (idx < len(my_list) and idxx.isdigit()):
        my_list[idx] = element
    return my_list
