#!/usr/bin/python3
""" square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square that inherits from Rectangle. """

    def __init__(self, size, x=0, y=0, id=None):
        """ Calls super class with parameters.
        Args:
            size: (int): Size of square.
            x: (int): X-cordinate.
            y: (int): Y-cordinate.
            id: (int): id of class instance.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Override of __str__ method of class Rectangle. """
        string = "[{}] ({}) {}/{} - {}"
        return (string.format(self.__class__.__name__, self.id, self.x,
                self.y, self.width))
