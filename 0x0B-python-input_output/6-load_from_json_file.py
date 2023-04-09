#!/usr/bin/python3
""" serialises data structure to json files"""
import json


def load_from_json_file(filename):
    """ createss an object from a JSON file """
    with open('filename', 'r', encoding="utf-8") as f:
        decoded_json = json.load(f)
        return decoded_json
