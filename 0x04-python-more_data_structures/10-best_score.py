#!/usr/bin/python3
def best_score(a_dictionary):
    temp = 0
    max_key = ''
    if a_dictionary is None:
        return (None)
    else:
        for key in a_dictionary:
            if a_dictionary[key] > temp:
                max_key = key
                temp = a_dictionary[key]
            else:
                continue
    return (max_key)
