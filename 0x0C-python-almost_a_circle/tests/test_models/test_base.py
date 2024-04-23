#!/usr/bin/python3
""" Unittest module for base.py """
import unittest

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """ The class shall be used to create test cases for base.py. """

    def setUp(self):
        """ Will automatically call for every single test run."""
        Base.__nb_objects = 0

    def test_init_without_id(self):
        """ Test without id. """
        base = Base()
        base2 = Base()
        self.assertEqual(base.id, 3)
        self.assertEqual(base2.id, 4)

    def test_init_with_id(self):
        """ Test with id. """
        base = Base(6)
        base2 = Base(22)
        self.assertEqual(base.id, 6)
        self.assertEqual(base2.id, 22)

    def test_to_json_string(self):
        """ Test obj conversion to JSON string. """
        rect = Rectangle(1, 7, 3, 8)
        dictionary = (rect.to_dictionary())
        json_dictionary = Base.to_json_string(sorted(dictionary.items()))
        self.assertEqual(json_dictionary, '[["height", 7], ["id", 10], '
                                        '["width", 1], ["x", 3], ["y", 8]]')
        base = Base.to_json_string([ { 'id': 12 }])
        self.assertEqual(base, '[{"id": 12}]')

    def test_save_to_file(self):
        """ Test file is created and saved """
        base = Base()
        base.save_to_file([])
        with open("Base.json", mode="r", encoding="utf-8") as file:
            self.assertEqual(file.read(), '[]')

        r1 = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r1])

        with open("Rectangle.json", "r") as file:
            lines = file.readlines()
        
        sorted_lines = sorted(lines)

        with open("Rectangle.json", "w") as file:
            file.writelines(sorted_lines)

        with open("Rectangle.json", "r") as file:
            sorted_contents = file.read()

        expected_contents = '[{"height": 7, "id": 8, "width": 10, "x": 2, "y": 8}]'

        Rectangle.save_to_file([Rectangle(1, 2)])
        with open("Rectangle.json", "r") as file:
            lines = file.readlines()

        sorted_lines = sorted(lines)

        with open("Rectangle.json", "w") as file:
            file.writelines(sorted_lines)

        with open("Rectangle.json", "r") as file:
            sorted_contents = file.read()

        expected_contents = '[{"height": 2, "id":3, "width": 1, "x": 0, "y": 0}]'
        
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), '[]')

    def test_from_json_string(self):
        """ Test list from json string conversion. """
        json_string = '[]'
        self.assertEqual(Base.from_json_string(json_string), [])

    def test_create(self):
        """ Test creation of rectangle and square. """
        dummy_rect_dict = {'width': 6, 'height': 12}
        rect = Rectangle.create(**dummy_rect_dict)
        self.assertIsInstance(rect, Rectangle)
        self.assertEqual(rect.width, 6)
        self.assertEqual(rect.height, 12)
        dummy_square_dict = {'size': 7}
        sq = Square.create(**dummy_square_dict)
        self.assertIsInstance(sq, Square)
        self.assertEqual(sq.size, 7)

    def test_load_from_file(self):
        """ Test loading JSON string from file to list of class instances. """
        obj_list = Base.load_from_file()
        self.assertEqual(obj_list, [])

        Rectangle.save_to_file([Rectangle(10, 7, 2, 8)])
        list_rectangles_output = Rectangle.load_from_file()

        self.assertEqual(list_rectangles_output[0].height, 7)

    def tearDown(self):
        """ Reset __nb_objects. """
        Base.__nb_objects = 0


if __name__ == "__main__":
    unittest.main()
