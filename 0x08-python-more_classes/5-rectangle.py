#!/usr/bin/python3

"""A module to test the functionality of the pythn class Module

It contains description of the class Rectangle.
"""


class Rectangle:
    """Defines the object Rectangle.

    Args:
        width: of type int, and implies the length in 'Meters'
        height: of type int, implies the vertical
        length of the object in 'Meters'
        """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''Retrieves the value of the width atrribute'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Sets the value of the Atrribute width

        checks:
        value must be an integer, otherwise TypeError is Raised
        Value must be >= 0, otherwise ValueError is Raised'''
        if not isinstance(value, int):
            raise TypeError('Width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        '''Retrieves the value of the width atrribute'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Sets the value of the Atrribute width

        checks:
        value must be an integer, otherwise TypeError is Raised
        Value must be >= 0, otherwise ValueError is Raised'''
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        '''Returns the Area of the object Rectangle'''
        return self.width * self.height

    def perimeter(self):
        '''Returns the Perimeter of the object Rectangle

            checks:
            if width or height is equals 0, method Return 0'''

        if (self.height == 0 or self.width == 0):
            return (0)
        else:
            return (2 * (self.height + self.width))

    def __str__(self):
        """Displays the object in a formated form.

        Replaces the Number of width and Heigth with the character #
        """
        rectangle = ''
        if self.width == 0 or self.height == 0:
            return rectangle
        
        rectangle = []
        for col in range(self.height):
            [rectangle.append('#') for row in range(self.width)]
            if col != self.height - 1:
                rectangle.append('\n')
        return ("".join(rectangle))

    def __repr__(self):
        """Returns the string representation of the object"""
        return f'Rectangle({self.width}, {self.height})'

    def __del__(self):
        """deletes an instance of the Rectangle class"""
        print('Bye Rectangle...')
