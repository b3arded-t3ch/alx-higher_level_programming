#!/usr/bin/python3
"""Defines an empty class"""


class BaseGeometry:
    """A Geometry class"""
    def area(self):
        """Raises a no-implementation Exception"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """validates an integer"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
