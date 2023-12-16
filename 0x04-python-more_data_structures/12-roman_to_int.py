#!/usr/bin/python3

def roman_to_int(roman_string):
    # Define a dict, where the key = roman figures, while the 'values' = integers
    code = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    # loop through the string to identify each char of the roman numeral.
    # - use a condition to check if "roman_string" = str or "None" value.
    # - add up value in the str
    for rom in roman_string:
        num = num + code[rom]
    return num
