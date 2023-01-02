#!/usr/bin/python3


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
