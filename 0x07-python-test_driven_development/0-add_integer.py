#!/usr/bin/python3
"""
module that is composed of a function that adds two integers
"""


def add_integer(a, b=98):
    """ a function that adds two integers.

    Args:
        a = the first integer.
        b = the second integer.

    Returns:
    the sum of two integers a & b

    Raises: TypeError if neither a or b is an integer or float
    """

    if not isinstance(a, float) and not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, float) and not isinstance(b, int):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)

    return a + b
