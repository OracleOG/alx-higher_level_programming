#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = list(set(my_list))
    sum = 0
    for x in new_list:
        sum = sum + x
    return sum
