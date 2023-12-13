#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    s_keys = list(sorted(a_dictionary))
    for keys in s_keys:
        print(f"{keys}: {a_dictionary[keys]}")


'''
def print_sorted_dictionary(a_dictionary):
    new_list = list(a_dictionary.keys())
    new_list.sort()
    for i in new_list:
        print("{}: {}" .format(i, a_dictionary.get(i)))
'''
