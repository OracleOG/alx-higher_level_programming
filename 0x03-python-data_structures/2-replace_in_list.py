#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    if idx < 0:
        return (None)
    x = len(my_list)
    if idx > (x - 1):
        return (None)
    my_list[idx] = element
    return (my_list)
