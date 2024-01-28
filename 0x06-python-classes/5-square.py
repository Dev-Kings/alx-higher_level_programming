#!/usr/bin/python3
"""
A module initializing class Square which defines a square.
"""


class Square:
    """This is an empty class at the moment.
    The __init__ method has checks if size is integer or less than 0.

    Args:
        size :(obj:'int', optional): Size of square. Defaults to 0.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.

    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """int: size of square.
            Raises:
                TypeError: if size is not integer.
                ValueError: If size is less than 0.
        """
        return (self.__size)

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Computes area.

        Returns:
            Square area.
        """
        return (self.__size ** 2)

    def my_print(self):
        """Prints the square with character #.
        """
        if self.__size == 0:
            print()
        else:
            print(self.__size * "#")
