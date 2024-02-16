#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def setUp(self):
        self.arg_1 = [3, 4, 6, 3, 2]
        self.arg_2 = [[5, 4, 6, 7], [10, 4]]
        self.arg_3 = "string instead of list"
        self.arg_4 = ["st", "r"]
        self.arg_5 = (4, 6)
        self.arg_6 = {'a': 4, 'b': 2}

    def test_list_integers(self):
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer(self.arg_1), 6)
        self.assertEqual(max_integer(self.arg_2), [10, 4])

    def test_strings(self):
        self.assertEqual(max_integer(self.arg_4), 'st')
        self.assertEqual(max_integer(self.arg_3), 't')

    def test_dictionary(self):
        self.assertRaises(KeyError, max_integer, self.arg_6)

    def test_tuple(self):
        self.assertEqual(max_integer(self.arg_5), 6)

    def test_int_argument(self):
        self.assertRaises(TypeError, max_integer, 5)
