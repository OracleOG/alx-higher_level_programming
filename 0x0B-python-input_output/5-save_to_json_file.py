#!/usr/bin/python3
""" Module that contains a function that write to atext file, using JSON
representation

"""

import json


def save_to_json_file(my_obj, filename):
    """ A function that write to atext file, using JSON
representation

    Args: my_obj - obj for JSOn representation
          filename - name of file
"""
    with open(filename, 'w', encoding="utf-8") as f:
        filedata = json.dump(my_obj, f)
