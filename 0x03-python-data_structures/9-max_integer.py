#!/usr/bin/python3
def max_integer(my_list=[]):
    list_len = len(my_list)
    if list_len == 0:
        return (None)
    else:
        temp = my_list[0]
        for i in range(list_len - 1):
            for item in my_list:
                if item > temp:
                    temp = item
                else:
                    continue
        return (temp)
