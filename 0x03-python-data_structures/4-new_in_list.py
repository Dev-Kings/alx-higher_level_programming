#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_length = len(my_list)
    if idx < 0 or idx >= list_length:
        return (my_list.copy())
    else:
        list_copy = my_list.copy()
        del(list_copy[idx])
        list_copy.insert(idx, element)
        return (list_copy)
