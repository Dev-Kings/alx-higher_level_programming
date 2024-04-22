#!/usr/bin/python3
""" Module with class Rectangle."""
from models.base import Base


class Rectangle(Base):
    """ Class Rectangle that inherits from Base class.
    Has private instance variables, width and height.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Calls super class with id.
        Assigns each argument to the right attribute.
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if int(width) <= 0:
            raise ValueError("width must be > 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if int(height) <= 0:
            raise ValueError("height must be > 0")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if int(x) < 0:
            raise ValueError("x must be >= 0")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if int(y) < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """ Gets the width of rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """ Sets the width of the rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if int(value) <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Gets the height of rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """ Sets the height of rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if int(value) <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Gets the x-cordinate of rectangle"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """ Sets the x-cordinate value"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if int(value) < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Gets the y cordinate of rectangle"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """ Sets the y cordinate of rectangle"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if int(value) < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Computes and returns area of rectangle. """
        return (self.__width * self.__height)

    def display(self):
        """ Prints Rectangle instance in stdout using character '#' """
        for y_iter in range(self.__y):
            print()
        for h_iter in range(1, self.__height + 1):
            for x_iter in range(self.__x):
                print(" ", end='')
            print("{}".format(self.__width * '#'))

    def __str__(self):
        """ Override of __str__ method of Rectangle class."""
        string = "[{}] ({}) {}/{} - {}/{}"
        return (string.format(self.__class__.__name__, self.id, self.__x,
                self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """ Assigns an argument to each attribute.
        Args:
            args: variable number of arguments.
            kwargs: dictionary containing named arguments and values.
        """
        if len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    setattr(self, 'id', args[i])
                elif i == 1:
                    setattr(self, 'width', args[i])
                elif i == 2:
                    setattr(self, 'height', args[i])
                elif i == 3:
                    setattr(self, 'x', args[i])
                elif i == 4:
                    setattr(self, 'y', args[i])
        elif len(kwargs) > 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Converts class object to dictionary.
        Returns:
            Dictionary representation of Rectangle class.
        """
        rectangle_dict = {}
        for key, value in self.__dict__.items():
            clean_key = key.replace('_Rectangle__', '')
            rectangle_dict[clean_key] = value
        return (rectangle_dict)
