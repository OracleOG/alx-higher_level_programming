#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# Last digit of 4205 is 5 and is less than 6 and not 0
if number >= 0:
    l_digit = number % 10
else:
    l_digit = number % -10
print(f"Last digit of {number} is {l_digit}", end=' ')

# if the last digit is greater than 5: the string and is greater than 5
# if the last digit is 0: the string and is 0
# if the last digit is less than 6 and not 0: the string -
# and is less than 6 and not 0

if(l_digit > 5):
    print(f"and is greater than 5")
elif(l_digit == 0):
    print(f"and is 0")
elif(l_digit < 6 and l_digit != 0):
    print(f"and is less than 6 and not 0")
