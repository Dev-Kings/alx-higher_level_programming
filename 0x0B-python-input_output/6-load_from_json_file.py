#!/usr/bin/python3
"""Module containing load_from_json_file function."""
import json


def load_from_json_file(filename):
    """Creates an object from JSON file.
    Args:
        filename: (string): Name of file to write to.
    """
    try:
        with open(filename, mode='r', encoding='utf-8') as my_file:
            return (json.load(my_file))
    except (FileNotFoundError, json.JSONDecodeError):
        return ([])
