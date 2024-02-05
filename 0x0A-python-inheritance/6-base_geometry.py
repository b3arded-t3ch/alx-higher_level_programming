#!/usr/bin/python3
"""Defines an empty class"""


class BaseGeometry:
    """A Geometry class"""
    def area(self):
        """Raises a no-implementation Exception"""
        raise Exception("area() is not implemented")
