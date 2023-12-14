#!/usr/bin/python3
from roman import fromRoman


def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return (0)
    else:
        return (fromRoman(roman_string))
