#!/usr/bin/python3

# Function that creates a copy of a string
# And removes a character at position n

def remove_char_at(str, n):
    if (n < 0 or n >= len(str)):
        return (str)
    else:
        new_str = str[:n] + str[n + 1:]
    return new_str
