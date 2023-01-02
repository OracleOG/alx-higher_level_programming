#!/usr/bin/python3


def no_c(my_string):
    x = len(my_string)
    j = 0
    new = my_string[:]

    for i in range(x):
        if (my_string[j] == 'c' or my_string[j] == 'C'):
            new = new[:i - j] + my_string[i + 1:]
            j += 1
    return (new)
