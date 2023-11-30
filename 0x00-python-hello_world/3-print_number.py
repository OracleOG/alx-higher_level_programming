#!/usr/bin/python3
number = 98
if not isinstance(number, int):
    raise ValueError("Variable 'number' must be an integer")
print(f"{number} Battery street")
