#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    if idx < 0:
        return (None)

    x = len(my_list) - 1
    if idx > x:
        return (None)
    else:
        new = my_list[:]
        new[idx] = element

        return (new)
