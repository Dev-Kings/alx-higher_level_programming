#!/usr/bin/python
"""Module with MyList class"""


class MyList(list):
    """Class inherits from super class list."""

    def print_sorted(self):
        """Custom function to print sorted list containing integers."""
        print(sorted(self))
