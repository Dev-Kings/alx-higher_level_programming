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

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance.
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
        return (json_dict)
