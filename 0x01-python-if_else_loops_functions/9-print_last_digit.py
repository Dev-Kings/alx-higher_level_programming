#!/usr/bin/env python3
def print_last_digit(number):
    last = 0
    if number == last:
        last = 0
    elif number < 0:
        number = number * -1
        last += number % 10
    else:
        last += number % 10
    print("{}".format(last), end='')
    return last
