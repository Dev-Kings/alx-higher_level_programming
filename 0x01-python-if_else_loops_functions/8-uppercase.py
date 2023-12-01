#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) > 96 and ord(c) < 123:
            print("{}".format(chr(ord(c) - 32)), end='')
        elif ord(c) > 64 and ord(c) < 91:
            print("{}".format(chr(ord(c))), end='')
        else:
            print("{}".format(c), end='')
    print()
