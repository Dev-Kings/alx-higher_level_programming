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
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(v, int) and v >= 0 for v in position):
            raise TypeError("position must be a tuple of 2 positive integers")

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

    @property
    def position(self):
        """tuple: position of square.
            Raises:
                TypeError: if position is nota tuple of two positive integers.
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        self.__position = value

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
            for j in range(self.__position[1]):
                    print()
            for i in range(self.__size):
                print(self.__position[0] * " " + self.__size * "#")
