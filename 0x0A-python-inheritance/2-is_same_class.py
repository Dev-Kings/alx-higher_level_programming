#!/usr/bin/python3
"""
Module with is_same_class function.
"""

def is_same_class(obj, a_class):
    """
    Checks if object is instance of class.
    Args:
        obj: (object): Object to check.
        a_class: (class): Class.
    Return:
        True if object is instance, False otherwise.
    """
    is_ = False
    if a_class == object:
        return (is_)
    if isinstance(obj, a_class):
        is_ = True
        return (is_)
    return (is_)
