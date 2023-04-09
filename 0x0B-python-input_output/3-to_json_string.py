#!/usr/bin/python3
""" module contains a function that seriolises data structures to json files.

"""

import json


def to_json_string(my_obj):
    """ a function that returns the JSON representation of an object.

    args: my_obj - object to be serialised:

    exception:
    raises no exceptions
"""

    filedata = json.dumps(obj)

    return filedata
