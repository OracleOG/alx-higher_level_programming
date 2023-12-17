#!/usr/bin/python3
for i in range(0, 9):
    num = i + 1
    for x in range(num, 10):
        if i != 8:
            print("{:d}{:d}".format(i, x), end='')
            print(" ,", end="")
        else:
            print("{:d}{:d}".format(i, x))