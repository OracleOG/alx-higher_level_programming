#!/usr/bin/python3

def best_score(a_dictionary):
    x = 0
    dicts = {'begin': 0}
    if a_dictionary is None or a_dictionary == {}:
        return None
    for keys, val in a_dictionary.items():
        if dicts['begin'] < val:
            x = keys
            dicts['begin'] = val

    return x
