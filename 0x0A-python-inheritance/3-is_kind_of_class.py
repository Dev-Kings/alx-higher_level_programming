#!/usr/bin/python3
"""
Module with is_kind_of_class function.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if object is instance of class, or parent class.
    Args:
        obj: (object): Object to check.
        a_class: (class): Class.
    Return:
        True if object is instance, False otherwise.
    """
    return (isinstance(obj, a_class))
