#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    if idx < 0:
        return (None)

    x = len(my_list) - 1
    if idx > x:
        return my_list

    new = my_list[:]
    new[idx] = element
    return (new)
