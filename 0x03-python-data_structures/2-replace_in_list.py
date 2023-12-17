#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    if idx < 0:
        return (my_list)
    x = len(my_list)
    if idx > (x - 1):
        return (my_list)
    my_list[idx] = element
    return (my_list)
