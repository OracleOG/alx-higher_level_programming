#!/usr/bin/python3


"""A module to test the functionality of the python class feature

This module contains a simple class called Rectangle"""


class Rectangle:
    """ a class that defines the properties of a rectangle
    """
    def __init__(self, width=0, height=0):
        """ a method that initialises the Rectangle object
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ method that returns the size of the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ method that sets the value of width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ method that returns the size of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ method that sets the value of height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
