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
        self.__width = value

    @property
    def height(self):
        """ Gets the height of rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """ Sets the height of rectangle"""
        self.__height = value

    @property
    def x(self):
        """ Gets the x-cordinate of rectangle"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """ Sets the x-cordinate value"""
        self.__x = value

    @property
    def y(self):
        """ Gets the y cordinate of rectangle"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """ Sets the y cordinate of rectangle"""
        self.__y = value
