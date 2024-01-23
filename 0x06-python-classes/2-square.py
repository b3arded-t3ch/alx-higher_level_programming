#!/usr/bin/python3
"""This defines a class square"""


class Square:
    """This models a square with size value"""

    def __init__(self, size=0):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must an integer")
        elif size < 0:
            raise TypeError("size must be an integer")
