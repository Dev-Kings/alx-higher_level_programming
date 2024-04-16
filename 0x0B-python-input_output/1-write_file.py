#!/usr/bin/python3
"""Module containing write_file function."""


def write_file(filename="", text=""):
    """Function writing a string to a text file.
    Args:
        filename: (string): Name of the file.
        text: (string): Content to write to file.
    Return:
        Number of characters written to file.
    """
    with open(filename, mode='w', encoding='utf-8') as my_file:
        return(my_file.write(text))
