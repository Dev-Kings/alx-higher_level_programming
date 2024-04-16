#!/usr/bin/python3
"""Module containing to_json_string function."""
import json

def to_json_string(my_obj):
    """Returns JSON representation of an object(string).
    Args:
        my_obj: (object): Object.
    Return:
        String representation.
    """
    s_rep = json.dumps(my_obj)
    return (s_rep)
