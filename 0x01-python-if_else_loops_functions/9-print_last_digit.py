#!/usr/bin/python3

def print_last_digit(number):
    number = abs(number)
    if number >= 0:
        l_digit = number % 10
    print("{:d}".format(l_digit), end='')

    return l_digit
