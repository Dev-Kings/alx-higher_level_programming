#!/usr/bin/python3
"""
A module containing class Rectangle.
"""


class Rectangle:
    """The class is empty at the moment.
    """
    def __init__(self, width=0, height=0):
        """Init method initializing private width and height.
        Args:
            width (int, optional): Width of rectangle.
            height (int, optional): Height of rectangle.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__width = width
            self.__height = height

    @property
    def width(self):
        """int: width of rectangle.
        Raises:
            TypeError: if not an integer.
            ValueError: if less than 0.
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """int: height of rectangle.
        Raises:
            TypeError: if not an integer.
            ValueError: if less than 0.
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            print("{} <= 0".format(value))
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
