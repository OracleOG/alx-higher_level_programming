#!/usr/bin/python3
""" a module that defines the class square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ a class that defines the object square """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id, x, y, size, size)

    def __str__(self):
        """ a str documentation for the object square """
        str_1 = f"[Square] ({self.id}) {self.x}/{self.y}"
        str_2 = f"{self.size}"
        return f"{str_1} - {str_2}"

    @property
    def size(self):
        """ getter for size """
        return self.size

    @size.setter
    def size(self, value):
        """ setter for size """
        self.width = value
        self.height = value
