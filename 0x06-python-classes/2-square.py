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
        try:
            try:
                assert type(size) == int
            except AssertionError:
                raise TypeError
            if size < 0:
                raise ValueError
            else:
                self.__size = size
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
