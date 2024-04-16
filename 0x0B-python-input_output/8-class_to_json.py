#!/usr/bin/python3
"""Module containing class_to_json function."""


def class_to_json(obj):
    """Returns the dictionary description for JSON
    serialization of an object.
    Args:
        obj: (object): Object to serialize.
    Return:
        Dictionary description.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("object is not serializable")

    json_dict = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[key] = value
        elif isinstance(value, (tuple, set)):
            json_dict[key] = list(value)
        elif hasattr(value, '__dict__'):
            json_dict[key] = class_to_json(value)
        else:
            raise TypeError(f"Unsupported data type for attribute '{key}'")

    return (json_dict)
