#!/usr/bin/python3


class Square:
    """ square defines the square of an object

    """
    def __init__(self, size=0):
        """ initialise method that stores the value of square size
        """
        if not isinstance(size, int):
            raise TypeError(" size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)
