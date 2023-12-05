#!/usr/bin/python3


def no_c(my_string):
    x = len(my_string)
    new = ''

    for i in range(x):
        if (my_string[i] == 'c' or my_string[i] == 'C'):
            continue
        new = new + my_string[i]
    return new
