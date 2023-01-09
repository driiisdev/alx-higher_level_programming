#!/usr/bin/python3
"""
This module supplies the class MyInt.
"""


class MyInt(int):
    """
    This class is a subclass  of int.
    """

    def __eq__(self, other):
        return self - other != 0

    def __ne__(self, other):
        return self - other == 0
