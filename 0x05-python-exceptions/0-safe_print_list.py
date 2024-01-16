#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        i = 0
        while i < x:
            count += 1
            print(my_list[i], end="")
            i += 1
        print()
        return (count)
    except IndexError:
        print()
        return (count - 1)
