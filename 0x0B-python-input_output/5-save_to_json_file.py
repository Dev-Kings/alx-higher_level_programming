#!/usr/bin/python3
"""Module containing save_to_json_file function."""
import json


def save_to_json_file(my_obj, filename):
    """Writes object to a text file, using a JSON representation.
    Args:
        my_obj: (object): Object to be converted.
        filename: (string): Name of file to write to.
    """
    with open(filename, mode='w', encoding='utf-8') as my_file:
        json.dump(my_obj, my_file)
