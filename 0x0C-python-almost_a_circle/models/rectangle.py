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
