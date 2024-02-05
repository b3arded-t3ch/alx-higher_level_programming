#!/usr/bin/python3
"""Defines class of Geometry"""


class BaseGeometry:
    """A Geometry class"""
    def area(self):
        """Raises a no-implementation Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates an integer
            Args:
                name (str): The name of the parameter.
                value (int): The parameter to validate.
            Raises:
                TypeError: If value is not an integer.
                ValueError: If value is <= 0.

        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """A rectangle child of class BaseGeometry
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
    """
    def __init__(self, width, height):
        """Initialising the attribuites of the sub class"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
