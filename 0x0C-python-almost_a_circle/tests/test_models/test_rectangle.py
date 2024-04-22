#!/usr/bin/python3
""" Unittest for rectangle.py """
import unittest

from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ The class shall be used to create test cases for rectangle module. """

    def test_init(self):
        """ Tests __init__ method. """
        rect = Rectangle(5, 10)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)

    def test_area(self):
        """ Tests area method. """
        rect = Rectangle(5, 10)
        self.assertEqual(rect.area(), 50)

    def test_display(self):
        """ Tests display method. """
        pass

    def test_str(self):
        """ Tests ___str__ method. """
        rect = Rectangle(5, 10, 1, 2, 99)
        self.assertEqual(str(rect), "[Rectangle] (99) 1/2 - 5/10")

    def test_update(self):
        """ Tests update method. """
        rect = Rectangle(5, 10, 1, 2, 99)
        rect.update(10, 20, 30, 40, 50)
        self.assertEqual(rect.id, 10)
        self.assertEqual(rect.width, 20)
        self.assertEqual(rect.height, 30)
        self.assertEqual(rect.x, 40)
        self.assertEqual(rect.y, 50)

    def test_to_dictionary(self):
        """ Tests to_dictionary method. """
        rect = Rectangle(5, 10, 1, 2, 99)
        rect_dict = {'id': 99, 'width': 5, 'height': 10, 'x': 1, 'y': 2}
        self.assertEqual(rect.to_dictionary(), rect_dict)


if __name__ == "__main__":
    unittest.main()
