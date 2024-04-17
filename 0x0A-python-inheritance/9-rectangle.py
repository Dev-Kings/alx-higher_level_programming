#!/usr/bin/python3
"""
Module containing class Rectangle that inherits from BaseGeometry class.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
Rectangle class.
"""


class Rectangle(BaseGeometry):
    """
    Class Rectangle, inherits from BaseGeometry class.
    """

    def __init__(self, width, height):
        """
        Instanciation.
        Args:
            width: Width of rectangle.
            height: Height of rectangle.
        """
        self.__width = super().integer_validator('width', width)
        self.__height = super().integer_validator('height', height)

    def area(self):
        """
        Calculates area of rectangle.
        """
        return (self.__width * self.__height)

    def __str__(self):
        """
        String representation of Rectangle class.
        Return:
            Rectangle description.
        """
        s = "[{}] {}/{}".format(self.__class__.__name__, self.__width,
                                self.__height)
        return (s)
