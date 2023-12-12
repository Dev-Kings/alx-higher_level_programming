#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for dk in sorted(list(a_dictionary)):
        print("{}: {}".format(dk, a_dictionary[dk]))
