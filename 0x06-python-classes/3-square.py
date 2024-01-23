#!/usr/bin/python3
"""Define a class square"""


class Square:
    """This models a square with size and its area"""

    def __init__(self, size=0):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """A method that returns the area of the square"""
        result = self.__size * self.__size
        return (result)
