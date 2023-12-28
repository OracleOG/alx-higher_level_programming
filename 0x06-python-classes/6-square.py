#!/usr/bin/python3


"""A module to test the functionality of the python "class" feature

This module contains the definition of a Class Square"""

class Square:
    """ Defines the object class.

    __init__ Args:
        size - is of no type and no value verification is done on it.
        position - use to create spaces in the my_print function
        """
    def __init__(self, size, position=(0, 0)):
        self.size = size
        self.position = position


    def area(self):
        """ Method that returns the square are of the object
        """
        return (self.__size ** 2)

    def my_print(self):
        """ Method that prints a # square according
        to the size value
        """
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(0, self.size):
                for k in range(self.position[0]):
                    print(" ", end='')
                for j in range(self.size):
                    print("#", end='')
                print()

    @property
    def size(self):
        """ Method to returns the size value
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Method to set the size value of the square object
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """ method that returns the position value
        """
        return self.__position
'''
    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        elif value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
'''

    @position.setter
    def position(self, value):
        """ Method that sets the position value of a square object
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
