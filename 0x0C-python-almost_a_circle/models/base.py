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
        if len(list_dictionaries) == 0 or list_dictionaries is None:
            return ("[]")
        js_string = json.dumps(list_dictionaries)
        return (js_string)
