#!/usr/bin/python3
"""Module containing from_json_string function."""
import json


def from_json_string(my_str):
    """Function that converts JSON string to object.
    Args:
        my_str: (JSON string): JSON string.
    Return:
        Object converted from JSON string.
    """
    obj = json.loads(my_str)
    return (obj)
