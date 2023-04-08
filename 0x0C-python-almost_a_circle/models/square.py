#!/usr/bin/python3
""" a module that defines the class square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ a class that defines the object square """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ a str documentation for the object square """
        str_1 = f"[Square] ({self.id}) {self.x}/{self.y}"
        str_2 = f"{self.size}"
        return f"{str_1} - {str_2}"

    @property
    def size(self):
        """ getter for size """
        return self.width

    @size.setter
    def size(self, value):
        """ setter for size """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ a method that updates the atrributes of the class square """

        atrr = ['id', 'size', 'x', 'y']

        if len(args) !=0 and args not None:
            for argv, num in zip(args, atrr):
                setattr(self, num, argv)
        else:
            for kw, value in kwargs.items():
                setattr(self, kw, value)
