#!/usr/bin/python3


def uppercase(str):

    new_str = ''
    for ch in str:
        asval = ord(ch)
        if asval >= 97 and asval <= 122:
            x = (asval - 96) + 64
            newchar = chr(x)
            new_str = new_str + newchar
        else:
            new_str = new_str + ch
    print("{}".format(new_str))
