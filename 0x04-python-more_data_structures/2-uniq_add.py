#!/usr/bin/python3
def uniq_add(my_list=[]):
    res = 0
    uniq_list = list(set(my_list))
    for x in uniq_list:
        res += x
    return (res)
