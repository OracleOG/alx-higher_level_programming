#!/usr/bin/python3
""" a module on creating base cases
"""


class Base:
    """ a class named base """
    __nd_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nd_objects += 1
            self.id = Base.__nd_objects
        else:
            self.id = id
