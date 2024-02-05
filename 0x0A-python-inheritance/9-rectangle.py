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
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """computes the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """prints string representation of the class"""
        class_info = "[" + str(self.__class__.__name__) + "] "
        class_info += str(self.__width) + "/" + str(self.__height)
        return class_info
