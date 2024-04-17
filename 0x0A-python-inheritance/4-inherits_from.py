#!/usr/bin/python3
"""
Module with inherits_from function.
"""


def inherits_from(obj, a_class):
    """
    Checks if object is instance of class that inherited from specified class.
    Args:
        obj: (object): Object to check.
        a_class: (class): Class.
    Return:
        True if object is instance and not same class, False otherwise.
    """
    return (isinstance(obj, a_class) and type(obj) != a_class)
