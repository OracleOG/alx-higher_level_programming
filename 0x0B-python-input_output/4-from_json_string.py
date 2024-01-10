#!/usr/bin/python3
import json

""" module that contains a function that returns on object represented
by a JSON string
"""


def from_json_string(my_str):
    """Function that returns an object represented by a JSON string

        Args:
            my_str - json formatted string"""
    return json.loads(my_str)
