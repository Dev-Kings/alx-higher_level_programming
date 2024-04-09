#!/usr/bin/python3
"""A module with LockedClass class."""


class LockedClass:
    """The class has setattr method.
    """

    def __setattr__(self, name="first_name"):
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

    def __dict__(self):
        """Returns a dictionary of instance attributes."""
        return (self.__dict__)
