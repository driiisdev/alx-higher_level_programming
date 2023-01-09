#!/usr/bin/python3

"""function that adds a new attribute to an object if its possible, otherwise, raise TypeError"""

def add_attribute(obj, a, v):
    """function that adds a new attribute to an object if its possible, else raise TypeError"""

    res = getattr(obj, "__doc__", None)
    if res is None:
        setattr(obj, a, v)
    else:
        raise TypeError("can't add new attribute")
