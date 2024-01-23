#!/usr/bin/python3
"""Defines class Square"""


class Square:
    """models a square with size and prints the square to stdout"""
    def __init__(self, size=0):
        """initialises the square with size attribute"""
        self.__size = size

    def area(self):
        """returns area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """prints # to stdout"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")

    @property
    def size(self):
        """gets size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
