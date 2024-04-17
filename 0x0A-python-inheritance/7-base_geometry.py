#!/usr/bin/python3
"""
BaseGeometry class.
"""


class BaseGeometry:
    """
    Contains area and integer_validator functions.
    """

    def area(self):
        """
        Raises:
            Exception if area is not implemented.
        """
        raise Exception("area() is not implementeid")

    def integer_validator(self, name, value):
        """
        Validates value.
        Args:
            name: (string): name of value.
            value: (int): value of name.
        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        return (int(value))
