#!/usr/bin/python3


"""A module to test the functionality of the python class feature

This module contains a simple class called Rectangle"""


class Rectangle:
    """ a class that defines the properties of a rectangle
    """
    def __init__(self, width, height):
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

    def height(self, value):
        """ method that sets the value of height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ method that calculates the area of a rectangle
        """
        return (self.height * self.width)

    def perimeter(self):
        """ method that calculates the perimeter of a rectangle
        """
        if (self.height == 0 or self.width == 0):
            return (0)
        else:
            return (2 * (self.height + self.width))

    def __str__(self):
        """ Method that returns the rectanglesize with '#'
        Returns: the string Rectangle in hash sign.
        """
        rectangle = ''
        if self.width == 0 or self.height == 0:
            return rectangle

        for i in range(self.height):
            rectangle += ("#" * self.width) + "\n"

        return rectangle[:-1]

    def __repr__(self):
        """ method returns the string representation of the rectangle class
        """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)
