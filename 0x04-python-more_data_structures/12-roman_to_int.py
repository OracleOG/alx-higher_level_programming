#!/usr/bin/python3

def roman_to_int(roman_string):
    # Define a dict, where the key = roman figures,
    # while the 'values' = integers
    if roman_string is None:
        return 0
    if not isinstance(roman_string, str):
        return 0
    code = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    strlen = len(roman_string) - 1
    # loop through the string to identify each char of the roman numeral.
    # - use a condition to check if "roman_string" = str or "None" value.
    # - add up value in the str
    for x, rom in enumerate(roman_string):
        if x < strlen:
            if code[rom] < code[roman_string[x + 1]]:
                num = num - code[rom]
            else:
                num = num + code[rom]
        else:
            num = num + code[rom]
    return num
