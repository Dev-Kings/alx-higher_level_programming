#!/usr/bin/python3

# Prints ASCII alphabet in reverse order
# Alternating uppercase and lower case
# Last letter 'z' is small , followed by upper 'Y'

for index in range(122, 96, -1):
    if index % 2 == 0:
        alphabet = chr(index)
    else:
        alphabet = chr(index - 32)
    print("{}".format(alphabet), end='')
