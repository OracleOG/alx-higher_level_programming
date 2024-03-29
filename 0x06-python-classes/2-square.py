#!/usr/bin/python3


"""A module to test the functionality of the python "class" feature

This module contains the definition of a Class Square"""


class Square:
    """ Defines the object class.

    Args:
        size - is of no type and no value verification is done on it.
        """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
