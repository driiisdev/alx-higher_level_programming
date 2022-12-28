#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    idxx = str(element)

    new_list = my_list[:len(my_list)]
    if (idx >= 0) and (idx < len(new_list) and idxx.isdigit()):
        new_list[idx] = element
        return new_list
    return my_list
