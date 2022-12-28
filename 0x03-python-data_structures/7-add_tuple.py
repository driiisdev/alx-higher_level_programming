#!/usr/bin/python3
def add_tuple(tuple_a, tuple_b):
    if len(tuple_a) == 1:
        c = tuple_a[0] + tuple_b[0], 0 + tuple_b[1]
    elif len(tuple_b) == 1:
        c = tuple_a[0] + tuple_b[0], tuple_a[1] + 0
    elif len(tuple_a) == 0:
        c = 0 + tuple_b[0], 0 + tuple_b[1]
    elif len(tuple_b) == 0:
        c = tuple_a[0] + 0, tuple_a[1] + 0
    elif len(tuple_b) == 1 and len(tuple_a) == 0:
        c = 0 + tuple_b[0], 0
    elif len(tuple_a) == 1 and len(tuple_b) == 0:
        c = tuple_a[0] + 0, 0
    elif len(tuple_b) == 0 and len(tuple_a) == 0:
        c = 0, 0
    elif len(tuple_b) == 1 and len(tuple_a) == 1:
        c = tuple_a[0] + tuple_b[0], 0
    else:
        c = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    return c
