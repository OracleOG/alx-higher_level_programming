#!/usr/bin/python3

def islower(c):
    asval = ord(c)
    if asval < 97 or asval > 122:
        return False
    elif asval >= 97 and asval <= 122:
        return True
