#!/usr/bin/python3
""" The module that finds a peak value from an unsorted list
"""


def find_peak(list_of_integers):
    """Function that returns the max element from unsorted list
    Argument:
        list_of_integer - which is the unsorted list
    """
    if not list_of_integers:
        return None

    u_list = list_of_integers
    length = len(u_list)
    midpoint = int(length / 2)

    # middle element is the only one in the list
    if midpoint - 1 < 0 and midpoint + 1 >= length:
        return u_list[midpoint]

    elif midpoint - 1 < 0:
        if u_list[midpoint] > u_list[midpoint + 1]:
            return u_list[midpoint]
        else:
            return u_list[midpoint + 1]

    elif midpoint + 1 >= length:
        if u_list[midpoint] > u_list[midpoint - 1]:
            return u_list[midpoint]
        else:
            return u_list[midpoint - 1]

    if u_list[midpoint - 1] < u_list[midpoint] > u_list[midpoint + 1]:
        return u_list[midpoint]

    if u_list[midpoint + 1] > u_list[midpoint - 1]:
        return find_peak(u_list[midpoint:])
    return find_peak(u_list[:midpoint])
