#!/usr/bin/python3
"""A module containing function that prints a square."""


def print_square(size):
    """Prints a square with the character #.
    Args:
        size (int): Size to be computed.
    Raises:
        TypeError: if size is not an integer,
                    if size is a float,
                    if size is less than 0.
        ValueError: if size is less than 0.
    """
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    size_int = int(size)
    square = size_int**2
    for i in range(size):
        print("{}".format(size*'#'))
