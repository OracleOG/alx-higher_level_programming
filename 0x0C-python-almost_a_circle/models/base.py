#!/usr/bin/python3
""" a module on creating base cases
"""
import json
import os.path


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

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the json string representation 'json_string'
"""
        if not json_string or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ creates an instance from the dictionary argument"""
        if cls.__name__ == "Rectangle":
            inst = cls(10, 5)
        else:
            inst = cls(10)
        inst.update(**dictionary)

        return inst

    @classmethod
    def load_from_file(cls):
        """ returns list of list of instances from a json string representation
of instances"""
        filename = "{}.json".format(cls.__name__)


        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r') as f:
            json_str = f.read()

        list_json_str = cls.from_json_string(json_str)

        list_inst = []

        for num in range(len(list_json_str)):
            list_inst.append(cls.create(**list_json_str[num]))

        return list_inst
