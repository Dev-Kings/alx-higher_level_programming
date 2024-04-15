#!/usr/bin/python3

def lookup(obj):
    """Returns list of attributes and methods of an object.
    Args:
        obj: (int, class): Object.
    Returns:
        A list object.
    """
    return (list(obj.__dict__))
