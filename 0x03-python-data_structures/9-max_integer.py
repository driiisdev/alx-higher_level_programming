#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == "" or len(my_list) == 0:
        return None
    d = my_list[0]
    for i in my_list:
        if (i > d):
            d = i
        else:
            continue
    return d
