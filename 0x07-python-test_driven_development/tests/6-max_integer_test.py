#!/usr/bin/python3
""" Unittest for max_integer([...])
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
    def test_stringInAList(self):
        with self.assertRaises(TypeError):
            max_integer([2,3,2,1,'a'])
    def test_anInt(self):
        with self.assertRaises(TypeError):
            max_integer(427)
    def test_aNull(self):
        with self.assertRaises(TypeError):
            max_integer(None)
