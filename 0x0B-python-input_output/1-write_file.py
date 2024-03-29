#!/usr/bin/python3
""" a module that writes to a file

"""


def write_file(filename="", text=""):
    """ a function that write a string to a file
    and returns the number of characters written to that file
    args: filename, text.

    returns: number of characters written to that file.

"""

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
