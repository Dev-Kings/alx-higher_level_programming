#!/usr/bin/python3
def no_c(my_string):
    string_list = []
    new_str = ""
    for s in my_string:
        if s ==  'c' or s == 'C':
            continue
        else:
            string_list.append(s)
            new_str += s
    return (new_str)
