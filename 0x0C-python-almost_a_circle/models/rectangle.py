#!/usr/bin/python3
""" a module tha defines the class rectnagle """
from models.base import Base


class Rectangle(Base):
    """ a class that defines a rectangle. """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ getter for private attr width """
        return self.__width

    @width.setter
    def width(self, value):
        """ getter for private attr width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 1:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ getter for private attr width """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for private attr width """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 1:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ getter for private attr width """
        return self.__x

    @x.setter
    def x(self, value):
        """ getter for private attr width """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ getter for private attr width """
        return self.__y

    @y.setter
    def y(self, value):
        """ getter for private attr width """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ returns the area of the object rectangle """
        return self.width * self.height

    def display(self):
        """ prints to stdout the rectangle instance with character '#' """
        for col in range(self.height):
            for row in range(self.width):
                print('#', end='')
            print()
