#!/usr/bin/python3


"""A module that tests the functionality of 'inheritance of python

Module contains the class MyList that inherits from the Base class 'list'"""


class MyList(list):
    """a CLASS THAT INHERITS FROM THE bASE CLASS LIST

        ARGS:
            list"""
    def print_sorted(self):
        """Method that Prints a sorted list,
        wiithout affecting the main list"""
        sorted = self[:]
        sorted.sort()
        print(sorted)
