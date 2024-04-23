#!/usr/bin/python3
""" Unittest for rectangle.py """
import sys
import unittest
from io import StringIO
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
        
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
        with self.assertRaises(TypeError):
            Rectangle(1, "2")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, -2)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_area(self):
        """ Tests area method. """
        rect = Rectangle(5, 10)
        self.assertEqual(rect.area(), 50)

    def test_display(self):
        """ Tests display method. """
        rect = Rectangle(2, 2)
        captured_output = StringIO()
        sys.stdout = captured_output
        
        rect.display()
        sys.stdout = sys.__stdout__

        displayed_output = captured_output.getvalue()
        expected_output = "##\n##\n"
        self.assertEqual(displayed_output, expected_output)

        rect2 = Rectangle(2, 2, 3)
        captured_output = StringIO()
        sys.stdout = captured_output

        rect2.display()
        sys.stdout = sys.__stdout__
        displayed_output = captured_output.getvalue()
        expected_output = "   ##\n   ##\n"
        self.assertEqual(displayed_output, expected_output)

    def test_str(self):
        """ Tests ___str__ method. """
        rect = Rectangle(5, 10, 1, 2, 99)
        self.assertEqual(str(rect), "[Rectangle] (99) 1/2 - 5/10")

    def test_width_getter_setter(self):
        """ Tests width getter and setter methods. """
        rect = Rectangle(5, 10)
        rect.width = 8
        self.assertEqual(rect.width, 8)

    def test_height_getter_setter(self):
        """ Tests height getter and setter methods. """
        rect = Rectangle(5, 10)
        rect.height = 4
        self.assertEqual(rect.height, 4)
        
    def test_height_setter_with_wrong_input(self):
        """ Tests height setter with wrong inputs. """
        rect = Rectangle(6, 10)
        with self.assertRaises(TypeError):
            rect.height = "55"

    def test_x_getter_setter(self):
        """ Tests x getter and setter methods. """
        rect = Rectangle(5, 10)
        rect.x = 14
        self.assertEqual(rect.x, 14)

    def test_y_getter_setter(self):
        """ Tests y getter and setter methods. """
        rect = Rectangle(5, 10)
        rect.y = 17
        self.assertEqual(rect.y, 17)

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
