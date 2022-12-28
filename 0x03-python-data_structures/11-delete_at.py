#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    leng = len(my_list)
    new = my_list
    if leng == 0 or idx >= leng or idx < 0:
        return my_list
    else:
        rem = new[idx]
        new.remove(rem)
    return new
