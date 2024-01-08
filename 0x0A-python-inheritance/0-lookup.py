#!/usr/bin/python3


"""A module to test the Functionality of "inheritance" in python

module contains a function called; 'lookup'  """

def lookup(obj):
    """Returns the list of Available attributes and methods of an object"""
    lists = [attr for attr in dir(obj)]
    return lists