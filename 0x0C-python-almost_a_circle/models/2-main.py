#!/usr/bin/python3
""" Check """
from square import Square
from rectangle import Rectangle

s = Square(5)
r = Rectangle(5,7)
print(s.__dict__)
print(r.__dict__)
print('----------------')
dict = {}
print (len(dict))
print('----------------')
r1 = Rectangle(10, 2, 1, 9)
print(r1)
r1_dictionary = r1.to_dictionary()
print(r1_dictionary)
print(type(r1_dictionary))
