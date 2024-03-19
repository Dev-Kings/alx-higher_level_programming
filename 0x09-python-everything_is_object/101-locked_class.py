#!/usr/bin/python3
"""A module with LockedClass class."""


class LockedClass:
    """The class has setattr method.
    """

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
        else:
            self.__dict__[name] = value

    def dict(self):
        """Returns the instance dictionary of attributes."""
        return (self.__dict__)
