#!/usr/bin/python3
""" Unittest module for square module. """
import unittest

from models.square import Square


class TestSquare(unittest.TestCase):
    """ The class shall be used to create test cases for square module."""

    def test_init(self):
        """ Tests __init__ method. """
        sq = Square(11)
        self.assertEqual(sq.width, 11)
        self.assertEqual(sq.height, 11)
        self.assertEqual(sq.x, 0)
        self.assertEqual(sq.y, 0)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("1")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "2")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "3")

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)
            Square(0)
        
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -2)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 2, -3)

    def test_str(self):
        """ Tests __str__ method. """
        sq = Square(5, 2, 3, 99)
        self.assertEqual(str(sq), "[Square] (99) 2/3 - 5")

    def test_size_getter_setter(self):
        """ Tests size getter and setter methods. """
        sq = Square(4)
        self.assertEqual(sq.size, 4)
        sq.size = 6
        self.assertEqual(sq.size, 6)
        self.assertEqual(sq.width, 6)
        self.assertEqual(sq.height, 6)

    def test_x_getter_setter(self):
        """ Tests x getter and setter methods. """
        sq = Square(5)
        sq.x = 7
        self.assertEqual(sq.x, 7)

    def test_y_getter_setter(self):
        """ Tests y getter and setter methods. """
        sq = Square(7)
        sq.y = 5
        self.assertEqual(sq.y, 5)

    def test_update(self):
        """ Tests update method. """
        sq = Square(5, 2, 3, 99)
        sq.update(10, 20, 30, 40)
        self.assertEqual(sq.id, 10)
        self.assertEqual(sq.size, 20)
        self.assertEqual(sq.x, 30)
        self.assertEqual(sq.y, 40)

    def test_to_dictionary(self):
        """ Tests to_dictionary method. """
        sq = Square(5, 2, 3, 99)
        sq_dict = {'id': 99, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(sq.to_dictionary(), sq_dict)


if __name__ == "__main__":
    unittest.main()
