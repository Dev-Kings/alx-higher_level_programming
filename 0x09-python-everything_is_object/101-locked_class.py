#!/usr/bin/python3
"""A module with LockedClass class."""


class LockedClass:
    """The class has setattr method.
    slots used to limit attributes to  a predefined list.
    """

    __slots__ = ['first_name']

    def __setattr__(self, name, value=None):
        """An override of setattr built-in.
        Args:
            name (string): instance attribute.
            value (string, optional): value to set.
        Raises:
            AttributeError: if name is not 'first_name'
        """
        if name != 'first_name':
            raise AttributeError("'LockedClass' object has no attribute '{}'"
                                 .format(name))
