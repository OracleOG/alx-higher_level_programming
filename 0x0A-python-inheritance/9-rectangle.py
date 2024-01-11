#!/usr/bin/python3


"""Module that demonstrates the functionality of the Python's 'inheri
tance'

    Contains the class BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that inherits from 'Bas
    eGeometry', it defines the object Rectangle.

        Args: width, height"""
    def __init__(self, width, height):
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """A method that computes the Area of a Rectangle

            Return: the product of width and height"""
        return self.__width * self.__height

    def __str__(self):
        """a method that returns a formated string when the class is printed"""
        return (f"[Rectangle] {self.__width}/{self.__height}")
