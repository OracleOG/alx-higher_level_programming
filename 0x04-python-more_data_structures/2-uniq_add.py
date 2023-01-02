#!/usr/bin/python3


def uniq_add(my_list=[]):
    no_dup = set(my_list)

    num = 0

    for x in my_list:
        num += x

    return (num)
