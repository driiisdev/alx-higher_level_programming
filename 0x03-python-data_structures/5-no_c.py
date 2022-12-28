#!/usr/bin/python3
def no_c(my_string):
    if my_string == "":
        return my_string
    else:
        b = 0
        for a in my_string:
            if a == "c":
                i = my_string.index("c", b)
                my_string = my_string[:i] + my_string[i + 1:]
                b = i + 1
            elif a == "C":
                i = my_string.index("C", b)
                my_string = my_string[:i] + my_string[i + 1:]
                b = i + 1
    return my_string
