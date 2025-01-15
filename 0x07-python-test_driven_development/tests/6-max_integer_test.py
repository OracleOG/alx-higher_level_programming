#!/usr/bin/python3
""" Unittest for max_integer([...])
Test Cases:
- if it returns the correct max integer.
- if the list contains a float.
- if the list contains big numbers.
- if the list contains big float numbers.
- if the list contains a string.
- if variable passed as parameter is not a list.
- if the list is empty.
- only negative numbers exist in the list.
- one negative number exists in the list.
- one element in the list.
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_isMax(self):
        self.assertEqual(max_integer([1,3,2,1,5,7]), 7)
    def test_containsFloat(self):
        self.assertEqual(max_integer([3,4,3.4,4.5]), 4.5)
    def test_bigNumbers(self):
        self.assertEqual(max_integer([39283, 3748,1984,8277,18934,77389]), 77389)
    def test_bigFloatNumbers(self):
        self.assertEqual(max_integer([39283.5, 3748.7,1984.9,8277.3,18934.2,77389.3]), 77389.3)
    def test_max_at_the_beginning(self):
        self.assertEqual(max_integer([7,2,3,4,5]), 7)
    def test_max_at_the_middle(self):
        self.assertEqual(max_integer([2,3,7,4,5]), 7)
    def test_max_at_the_end(self):
        self.assertEqual(max_integer([2,3,4,5,7]), 7)
    def test_emptyList(self):
        self.assertEqual(max_integer([]), None)
    def test_onlyNegativeNumbers(self):
        self.assertEqual(max_integer([-1,-2,-3,-4,-5]), -1)
    def test_oneNegativeNumbers(self):
        self.assertEqual(max_integer([1,2,3,4,-5]), 4)
    def test_oneElement(self):
        self.assertEqual(max_integer([1]), 1)
    def test_stringInAList(self):
        with self.assertRaises(TypeError):
            max_integer([2,3,2,1,'a'])
    def test_anInt(self):
        with self.assertRaises(TypeError):
            max_integer(427)
    def test_aNull(self):
        with self.assertRaises(TypeError):
            max_integer(None)
