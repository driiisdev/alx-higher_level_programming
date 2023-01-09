#!/usr/bin/python3

"""function that adds a new attribute to an object if its possible"""

def add_attribute(obj, a, v):
    """function that adds a new attribute to an object if its possible, else raise TypeError"""

    res = getattr(obj, "__doc__", None)

    """using if/else statement instead of try/except"""
    if res is None:
        """setattr if obj gotten is none"""
        setattr(obj, a, v)
    elif not setattr(obj, a, v):
        """if  not setattr, raise error"""
        raise TypeError("can't add new attribute")
    else:
        raise TypeError("can't add new attribute")
