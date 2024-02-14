#!/usr/bin/python3
"""Addition module.
This module adds integers.
"""

def add_integer(a, b=98):
    """Adds a and b; a and b must be integers or floats
    in order for addition to take place.
    Args:
        a (int, float): First number
        b (int, float, optional): Second number
    Raises:
        TypeError: if either param is not int or float
    Returns:
        Summation of a and b.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
