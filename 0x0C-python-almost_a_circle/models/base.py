#!/usr/bin/python3
""" Module containing Base class."""


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
