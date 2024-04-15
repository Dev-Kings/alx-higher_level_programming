#!/usr/bin/python3
"""Module with MyList class. MyList class inherits from list super class."""


class MyList(list):
    """Class inherits from super class list. The class then implements
    printing of list in ascending order.
    """

    def print_sorted(self):
        """Custom function to print sorted list containing integers."""
        print(sorted(self))
