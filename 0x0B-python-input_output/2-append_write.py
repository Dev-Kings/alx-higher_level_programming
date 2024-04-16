#!/usr/bin/python3
"""Module containing append_write function."""


def append_write(filename="", text=""):
    """Appends a string at end of a text file.
    Args:
        filename: (string): Name of file.
        text: (string): Content to append.
    """
    chars_written = 0
    with open(filename, mode='a', encoding='utf-8') as my_file:
        chars_written = my_file.write(text)
        return (chars_written)
