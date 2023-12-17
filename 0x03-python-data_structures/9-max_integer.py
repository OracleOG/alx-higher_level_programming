#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    x = my_list[0]
    for row in my_list:
        if x < row:
            x = row
    return x
