#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    new_dict = {}
    for dk in a_dictionary:
        if key == dk:
            new_dict[key] = value
            a_dictionary[dk] = value
        else:
            new_dict[dk] = a_dictionary[dk]
            new_dict[key] = value
    a_dictionary[key] = value
    return (new_dict)
