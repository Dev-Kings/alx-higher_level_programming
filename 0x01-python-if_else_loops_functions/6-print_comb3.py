#!/usr/bin/python3
for first_num in range(0, 10):
    for second_num in range(first_num, 10):
        if first_num == 0 and second_num == 0:
            continue
        elif first_num == second_num:
            continue
        else:
            print("{}{}".format(first_num, second_num), end=', ')
print()
