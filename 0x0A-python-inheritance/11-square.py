#!/usr/bin/python3
"""
Module containing class Square that inherits from Rectangle class.
"""
Rectangle = __import__('9-rectangle').Rectangle

"""
Square class.
"""


class Square(Rectangle):
    """
    Class Sqaure, inherits from Rectangle class.
    """

    def __init__(self, size):
        """
        Instanciation.
        Args:
            size: Size of one side.
        """
        self.__size = super().integer_validator('size', size)

    def area(self):
        """
        Calculates area of square.
        Return:
            Area.
        """
        return (self.__size**2)

    def __str__(self):
        """
        String representation of Rectangle class.
        Return:
            Rectangle description.
        """
        s = "[{}] {}/{}".format(
                self.__class__.__name__, self.__size,
                self.__size)
        return (s)
