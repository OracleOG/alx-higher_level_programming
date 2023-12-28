#!/usr/bin/python3


"""A module to test the functionality of the python "class" feature

This module contains the definition of a Class Square"""

class Square:
    """Defines the object class.

    Args:
    param (int): size of the square -  has no type and no value verification is done on it."""
    def __init__(self, size):
        self.__size = size
