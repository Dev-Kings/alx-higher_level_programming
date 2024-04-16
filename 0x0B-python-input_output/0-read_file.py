#!/usr/bin/python3
"""Module with read_file function."""


def read_file(filename=""):
    """This function reads a text file with UTF8 encoding."""
    with open(filename, mode='r', encoding='utf-8') as my_file:
        for line in my_file:
            print(line, end='')
