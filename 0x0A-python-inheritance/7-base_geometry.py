#!/usr/bin/python3


"""Module that demonstrates the functionality of the Python's 'inheritance'

    Contains the class BaseGeometry"""


class BaseGeometry:
    """An empty class"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method validate the variable 'value'

            Args: name, value"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
