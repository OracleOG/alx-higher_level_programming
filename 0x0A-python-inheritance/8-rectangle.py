#!/usr/bin/python3


"""Module that demonstrates the functionality of the Python's 'inheritance'

    Contains the class BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that inherits from 'BaseGeometry',
     it defines the object Rectangle.

        Args: width, height"""
    def __init__(self, width, height):
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
