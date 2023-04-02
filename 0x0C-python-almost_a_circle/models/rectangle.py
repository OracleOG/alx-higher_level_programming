#!/usr/bin/python3
""" a module tha defines the class rectnagle """
from models.base import Base


class Rectangle(Base):
    """ a class that defines a rectangle. """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """ getter for private attr width """
        return self.__width

    @width.setter
    def width(self, value):
        """ getter for private attr width """
        self.name = value

    @property
    def height(self):
        """ getter for private attr width """
        return self.__height

    @height.setter
    def height(self, value):
        """ getter for private attr width """
        self.name = value

    @property
    def x(self):
        """ getter for private attr width """
        return self.__x

    @x.setter
    def x(self, value):
        """ getter for private attr width """
        self.name = value

    @property
    def y(self):
        """ getter for private attr width """
        return self.__y

    @y.setter
    def y(self, value):
        """ getter for private attr width """
        self.name = value
