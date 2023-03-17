#!/usr/bin/python3
""" a module on creating base cases
"""

class Base:
    __nd_objects = 0

    def __init__(self, id=None):
        if id == None:
            Base.__nd_objects += 1
            self.id = Base.__nd_objects
        else:
            self.id = id
