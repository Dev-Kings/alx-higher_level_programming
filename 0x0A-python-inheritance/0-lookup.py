#!/usr/bin/python3
"""Module with function to lookup attributes and methods of an object."""


def lookup(obj):
    """Returns list of attributes and methods of an object.
    Args:
        obj: (int, class): Object.
    Returns:
        A list object.
    """
    return (dir(obj))
