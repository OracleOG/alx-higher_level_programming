#!/usr/bin/python3
""" module that reads the data of a file
"""

def read_file(filename=""):
    """ function reads a file and writes it out to stdout

"""
    with open (filename, 'r', encoding ="utf-8") as f:
        file_data = f.read()
        print(file_data, end='')
