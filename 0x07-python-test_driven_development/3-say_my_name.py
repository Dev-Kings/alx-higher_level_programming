#!/usr/bin/python3
"""A module that containing a functionn that
prints fullname.
"""


def say_my_name(first_name, last_name=""):
    """Prints fullname.
    Args:
        first_name (str): Firstname.
        last_name (str, optional): Lastname
    Raises:
        TypeError: if first_name or last_name is not a string.
    """
    if first_name is None:
        print("No first name")
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
