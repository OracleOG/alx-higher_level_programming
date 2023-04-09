#!/usr/bin/python3
""" a module on creating base cases
"""
import json


class Base:
    """ a class named base """
    __nd_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nd_objects += 1
            self.id = Base.__nd_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the json string representation of list_objs to a file.
"""
        filename = "{}.json".format(cls.__name__)
        dict_list = []

        if list_objs is None:
            pass
        else:
            for objs in list_objs:
                dict_list.append(objs.to_dictionary())

        json_dict = cls.to_json_string(dict_list)

        with open(filename, 'w', encoding="utf-8") as f:
            f.write(json_dict)
