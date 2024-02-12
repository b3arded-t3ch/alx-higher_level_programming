#!/usr/bin/python3
"""This Defines class square"""


class Square(Rectangle):
    """Represents a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initiating a new square instance with Square's attributes"""
        super().__init__(id, x, y, size)

    def __str__(self):
        """returns  string format of the object"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @propety
    def size(self):
        """gets the square size"""
        return self.__size

    @size.setter
    def size(self, size):
        """sets width value"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size <= 0:
            raise ValueError("size must be > 0")
        self.__size = size

    def update(self, *args, **kwargs):
        """Assigns attribute to each command argument"""
        if args:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        else:
            if 'id' in kwargs and kwargs['id'] is not None:
                self.id = kwargs['id']
            if 'size' in kwargs and kwargs['size'] is not None:
                self.size = kwargs['size']
            if 'x' in kwargs and kwargs['x'] is not None:
                self.x = kwargs['x']
            if 'y' in kwargs and kwargs['y'] is not None:
                self.y = kwargs['y']

    def def to_dictionary(self):
        """returns the dictionary representation of square"""
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }
