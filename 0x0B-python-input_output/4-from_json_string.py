#!/usr/bin/python3
""" module that contains a function that returns on object represented
by a JSON string
"""
import json


def from_json_string(my_str):
    """ a function that returns an object represented by its JSON string
"""
    filedata = json.load(my_str)
    return filedata
