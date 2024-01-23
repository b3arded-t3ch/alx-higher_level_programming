#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Models a typical square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialising the attributes"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """get size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        elif value < 0:
            raise ValueError("value must >= 0")
        self.__size = value

    @property
    def position(self):
        """get current positio of the square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integer")
        if not isinstance(value[0], int) or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integer")
        if not isinstance(value[1], int) or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """Returns area of square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints square with # character"""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
