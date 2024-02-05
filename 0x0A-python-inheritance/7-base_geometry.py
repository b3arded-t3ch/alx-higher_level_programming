#!/usr/bin/python3
"""Defines an empty class"""


class BaseGeometry:
    """A Geometry class"""
    def area(self):
        """Raises a no-implementation Exception"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """validates an integer"""
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
