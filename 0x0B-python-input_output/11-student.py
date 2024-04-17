#!/usr/bin/python3
"""Module with class Student."""


class Student:
    """Class Student.
    The __init__ method assigns the first_name, last_name and age.
    Args:
        first_name: (string): The first name.
        last_name: (string): The last name.
        age: (int): Age of student.
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance.
        Only attributes contained in attrs is retrieved, else all attributes.
        Args:
            attrs: (list): List of string attributes.
        Return:
            Dictionary containing filtered keys/values.
        Raises:
            TypeError: If object is not serializable or unsupported data type.
        """
        if not hasattr(self, '__dict__'):
            raise TypeError("object is not serializable")
        json_dict = {}
        for key, value in self.__dict__.items():
            if isinstance(value, (list, dict, str, int, bool)):
                json_dict[key] = value
            elif isinstance(value, (tuple, set)):
                json_dict[key] = list(value)
            elif hasattr(value, '__dict__'):
                json_dict[key] = to_json(value)
            else:
                raise TypeError(f"Unsupported data type for attribute '{key}'")

        if isinstance(attrs, list):
            filtered_dict = {}
            for attr in attrs:
                if attr in json_dict:
                    filtered_dict[attr] = json_dict[attr]
            return (filtered_dict)
        else:
            return (json_dict)

    def reload_from_json(self, json):
        """Replaces all attributes of Student instance.
        Args:
            json: (dictionary): Dictionary of public attribute name
                                and value.
        """
        self.first_name = json['first_name']
        self.last_name = json['last_name']
        self.age = json['age']
