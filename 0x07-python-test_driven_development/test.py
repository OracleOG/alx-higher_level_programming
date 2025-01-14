#!/usr/bin/python3


"""
A module to aid the test of the unittest && Doctest function of python

The module contains a funncton 'add_integer'
"""

def add_integer(a, b=98):
    """A function a adds two integers

    Args: a & b
    these are the two integers to be added"""
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    return a + b