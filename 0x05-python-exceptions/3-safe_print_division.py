#!/usr/bin/python3


def safe_print_division(a, b):

    try:
        c = a / b
        return c
    except (TypeError, ValueError, ZeroDivisionError):
        c = None
        return c
    finally:
        print("Inside result: {}".format(c))
