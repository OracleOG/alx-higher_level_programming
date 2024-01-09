#!/usr/bin/python3


"""A module to test the functionality of 'input & output'

it contains the function read_file"""


def read_file(filename=""):
    """A function that reads a text file and prints it out n stdout

        args:
            filename: is the file o be printed"""
    with open(filename) as f:
        for line in f:
            print(line, end='')
