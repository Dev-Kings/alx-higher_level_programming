#!/usr/bin/python3
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
