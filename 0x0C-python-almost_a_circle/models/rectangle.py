#!/usr/bin/python3
"""Module for rectangle class"""
from modules.base import Base


class Rectangle(Base):
    """A representation of rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initiating a new instance with the attributes"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Gets width attribute"""
        return self.__width
    @property
    def height(self):
        """gets attr height"""
        return self.__height
    @property
    def x(self):
        """gets attr x"""
        return self.__x
    @property
    def y(self):
        """gets attr y"""
        return self.__y

    @width.setter
    def width(self, width):
        """sets width value"""
        self.validate_integer("width", width)
        self.__width = width

    @height.setter
    def height(self, height):
        """sets width value"""
        self.validate_integer("height", height)
        self.__height = height

    @x.setter
    def x(self, x):
        """sets width value"""
        self.validate_integer("x", x)
        self.__x = x

    @y.setter
    def y(self, y):
        """sets width value"""
        self.validate_integer("y", y)
        self.__y = y

    def validate_integer(self, name, value, eq=True):
        """Method for validating integers"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        elif not eq and value < 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        """This function returns the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """prints the Rectangle instance with the character # to stdout"""
        if self.width == 0 or self.height == 0:
            print("")
            return
        for i in range(self.y, self.y + self.height):
            for k in range(self.x, self.x + self.width):
                print('#', end="")
            print()

    def __str__(self):
        """returns a string representation of the class instance"""
        return f"[Rectangle] ({self.id}) {self.x/self.y} - {self.width/self.height}"

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if args:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        else:
            if 'id' in kwargs and kwargs['id'] is not None:
                self.id = kwargs['id']
            if 'width' in kwargs and kwargs['width'] is not None:
                self.width = kwargs['width']
            if 'height' in kwargs and kwargs['height'] is not None:
                self.height = kwargs['height']
            if 'x' in kwargs and kwargs['x'] is not None:
                self.x = kwargs['x']
            if 'y' in kwargs and kwargs['y'] is not None:
                self.y = kwargs['y']

    def to_dictionary(self):
        """converts the rectangle object to dict"""
        return {
                "id": self.id,
                "width":self.width,
                "height":self.height,
                "x":self.x,
                "y":self.y
                }
