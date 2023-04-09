#!/usr/bin/python3
""" a module that appends a string to the end of a file.

"""


def append_write(filename="", text=""):
    """ a function that appends a string to the end of a file


    args: filename, text

    exception: no exceptions raised.

"""
    with open(filename, 'a+', encoding="utf-8") as f:
        filedata = f.write(text)

        return filedata
