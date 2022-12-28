#!/usr/bin/python3

"""
This is a module that provides a MagicClass Object for a
Circle which has a private instance attribute "radius"
which must either be float or integer.
This class has a method to calculate the area of the circle
and a method to calculate the circumference of the circle
"""

import dis
import math


class MagicClass:

    """
    This is a class Object for a
    Circle which has a private instance attribute "radius"
    which must either be float or integer.
    This class has a method to calculate the area of the circle
    and a method to calculate the circumference of the circle
    """

    def __init__(self, radius=0):
        if type(radius) != float and type(radius) != int:
            raise TypeError("radius must  be a number")
        else:
            self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    def area(self):
        return (math.pi * (self.__radius ** 2))

    def circumference(self):
        return (2 * math.pi * self.__radius)

