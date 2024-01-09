#!/usr/bin/python3


"""A module that tests the functionality of 'inheritance of python

Module contains the class MyList that inherits from the Base class 'list'"""


class MyList(list):
    def print_sorted(self):
        self.sort()
        print(self)
