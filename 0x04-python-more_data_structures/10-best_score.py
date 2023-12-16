#!/usr/bin/python3

def best_score(a_dictionary):
    x = 0
    dicts = {'begin': 0}
    if a_dictionary == None:
        return None
    for keys, val in a_dictionary.items():
        if dicts['begin'] < val:
            x = keys
            dicts['begin'] = val
        
    return x

'''
def best_score(a_dictionary):
    list_keys = list(a_dictionary.keys())

    for i in list_keys:
        for x in list_keys:
            if a_dictionary[i] >= a_dictionary
            best = i
            break

    return (best)
'''