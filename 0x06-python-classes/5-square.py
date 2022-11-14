#!/usr/bin/python3


class Square:
    """ a class that defines the object square
    """
    def __init__(self, size):
        """ Method to initialize the square object
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Method that returns the square are of the object
        """
        return (self.__size ** 2)

    def my_print(self):
        if self.__size == 0:
            print()
        else:
             for i in range(self.__size):
                for y in range(self.__size):
                    print("#", end='')
                print()
                
    @property
    def size(self):
        """ Method to returns the size value
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Method to set the size value of the square object
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
