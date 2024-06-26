#!/usr/bin/python3
""" Unittest module for base.py """
import unittest
import json
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
        base = Base.to_json_string(None)
        self.assertEqual(type(base), str)
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(11, 1, 3, 4)
        dict1 = r1.to_dictionary()
        dict2 = r2.to_dictionary()
        json_dict1 = [{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]
        json_dict2 = [{"x": 3, "width": 11, "id": 1, "height": 1, "y": 4}]
        json_string = Base.to_json_string([dict1, dict2])
        self.assertNotEqual(dict1, json_dict1)
        self.assertNotEqual(dict2, json_dict2)
        self.assertEqual(type(dict1), dict)
        self.assertEqual(type(json_string), str)
        result = Base.to_json_string(None)
        self.assertEqual(result, "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertTrue(type(Base.to_json_string(None)) is str)
        self.assertTrue(type(Base.to_json_string("[]")) is str)
        self.assertTrue(type(json_string), str)
        d = json.loads(json_string)
        self.assertEqual(d, [dict1, dict2])
        json_string = Base.to_json_string([{'id': 12}])
        self.assertEqual(json_string, '[{"id": 12}]')

    def test_save_to_file(self):
        """ Test file is created and saved """
        base = Base()
        base.save_to_file([])
        with open("Base.json", mode="r", encoding="utf-8") as file:
            self.assertEqual(file.read(), '[]')

        Base.save_to_file(None)
        with open("Base.json", "r") as file:
            self.assertEqual(file.read(), '[]')

        Square.save_to_file([])
        with open("Square.json", "r") as file:
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

        try:
            os.remove("Rectangle.json")
        except Exception:
            pass

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), '[]')

        try:
            os.remove("Square.json")
        except Exception:
            pass

        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), '[]')
        try:
            os.remove("Square.json")
        except Exception:
            pass

        Square.save_to_file([Square(1)])
        with open("Square.json", "r") as file:
            self.assertEqual(len(file.read()), 39)

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

        sq1 = Square(5)
        sq2 = Square(7, 9, 1)
        list_sq = [sq1, sq2]
        Square.save_to_file(list_sq)
        list_sq_out = Square.load_from_file()
        self.assertNotEqual(id(list_sq[0]), id(list_sq_out[0]))
        self.assertEqual(str(list_sq[1]), str(list_sq[1]))

    def test_load_from_empty_file(self):
        """ Tests for load_from_file when empty. """
        try:
            os.remove("Rectangle.json")
        except Exception:
            pass
        open("Rectangle.json", 'a').close()
        self.assertEqual(Rectangle.load_from_file(), [])

    def tearDown(self):
        """ Reset __nb_objects. """
        Base.__nb_objects = 0


if __name__ == "__main__":
    unittest.main()
