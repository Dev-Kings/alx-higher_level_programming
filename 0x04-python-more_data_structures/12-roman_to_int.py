#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return (0)
    else:
        roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                          'D': 500, 'M': 1000}
        result = 0
        prev_value = 0

        for num in reversed(roman_string):
            value = roman_numerals[num]

            if value < prev_value:
                result -= value
            else:
                result += value
            prev_value = value
    return (result)
