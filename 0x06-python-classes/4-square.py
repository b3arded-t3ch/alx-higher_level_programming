#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Models a square with size, area and ability to mutate the size"""

    def __init__(self, size):
        """Initialises size attribute of the square"""
        self.__size = size

    def area(self):
        """Returns the area of the square"""
        result = self.__size * self.__size
        return (result)

    @property
    def size(self):
        """method to retrieve size attribute"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """method to update size attribute"""
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
