#!/usr/bin/python3


def safe_print_division(a, b):

    try:
        c = a / b
    except (TypeError, ValueError, ZeroDivisionError):
        c = None
        return c
    finally:
        print("Inside result: {}".format(c))
        return c

'''        
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result:{}".format(result))
        return (result)
'''