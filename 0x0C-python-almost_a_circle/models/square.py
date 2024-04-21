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

    @property
    def size(self):
        """ Gets the size of square."""
        return (self.width)

    @size.setter
    def size(self, size):
        """ Sets size of square."""
        if type(size) is not int:
            raise TypeError("width must be an integer")
        if int(size) <= 0:
            raise ValueError("width must be > 0")
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """ Updates value of class attributes.
        Args:
            args: variable number of arguments.
            kwargs: dictionary containing named arguments and values.
        """
        if len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    if type(args[i]) is not int:
                        raise ValueError("id must be an integer")
                    self.id = args[i]
                elif i == 1:
                    if type(args[i]) is not int:
                        raise TypeError("width must be an integer")
                    if int(args[i]) <= 0:
                        raise ValueError("width must be > 0")
                    self.width = args[i]
                    self.height = args[i]
                elif i == 2:
                    if type(args[i]) is not int:
                        raise TypeError("x must be an integer")
                    if int(args[i]) < 0:
                        raise ValueError("x must be >= 0")
                    self.x = args[i]
                elif i == 3:
                    if type(args[i]) is not int:
                        raise TypeError("y must be an integer")
                    if int(args[i]) < 0:
                        raise ValueError("y must be >= 0")
                    self.y = args[i]
        elif len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == 'id':
                    if type(value) is not int:
                        raise TypeError("id must be an integer")
                    self.id = value
                elif key == 'size':
                    if type(value) is not int:
                        raise TypeError("width must be an integer")
                    if int(value) <= 0:
                        raise ValueError("width must be > 0")
                    self.width = value
                    self.height = value
                elif key == 'x':
                    if type(value) is not int:
                        raise TypeError("x must be an integer")
                    if int(value) < 0:
                        raise ValueError("x must be >= 0")
                    self.x = value
                elif key == 'y':
                    if type(value) is not int:
                        raise TypeError("y must be an integer")
                    if int(value) < 0:
                        raise ValueError("y must be > 0")
                    self.y = value
