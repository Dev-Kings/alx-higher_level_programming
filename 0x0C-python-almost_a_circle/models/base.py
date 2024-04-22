#!/usr/bin/python3
""" Module containing Base class."""
import json


class Base:
    """ Class base with constructor and private attribute
    __nb__objects as 0.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Manages id of future classes.
        Args:
            id: (int): Number to assign to id of class instances.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Converts list of dictionary to JSON string.
        Args:
            list_dictionaries: (list): List of dictionary.
        Return:
            JSON string representation of list_dictionaries.
        """
        if not list_dictionaries:
            return ("[]")
        js_string = json.dumps(list_dictionaries)
        return (js_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON representation of list_objs to a file.
        Args:
            list_objs: (list): List of instances who inherits of Base class.
        """
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        json_string = cls.to_json_string(
                [obj.to_dictionary() for obj in list_objs])

        with open(filename, mode="w", encoding="utf-8") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """ Computes list of JSON string representation.
        Args:
            json_string: (string): JSON string.
        Return:
            List of JSON stringa after conversion.
        """
        list_from_json = []
        if json_string is None:
            return (list_from_json)
        list_from_json = json.loads(json_string)
        return (list_from_json)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attribute set.
        Args:
            dictionary: (dict): Dictionary representation of an instance.
        """
        if cls.__name__ == "Rectangle":
            from models.rectangle import Rectangle
            dummy_rectangle = Rectangle(5, 10)
            dummy_rectangle.update(**dictionary)
            return (dummy_rectangle)
        elif cls.__name__ == "Square":
            from models.square import Square
            dummy_square = Square(8)
            dummy_square.update(**dictionary)
            return (dummy_square)

    @classmethod
    def load_from_file(cls):
        """ Loads JSON string representation of a class and converts to
        a list of instances.
        """
        filename = cls.__name__ + ".json"
        class_instances = []
        try:
            json_string = ''
            with open(filename, encoding='utf-8') as file:
                json_string = file.read()
            list_dict_from_json = cls.from_json_string(json_string)
            for item in list_dict_from_json:
                class_instances.append(cls.create(**item))
            return (class_instances)
        except FileNotFoundError:
            return (class_instances)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes the CSV serialization of a list of objects to a file.
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Instantiates classes from a CSV file.
        Reads from `<cls.__name__>.csv`.
        Returns:
            list: A list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    filenames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
            except IOError:
                return []
