#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new = []
    for row in my_list:
        if row % 2 == 0:
            new.append(True)
        elif row % 2 == 1:
            new.append(False)
    return new
