#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return (0)
    else:
        res = 0
        second_tup_num_sum = 0
        for tup in my_list:
            result = 1
            second_tup_num_sum += tup[1]
            for num in tup:
                result *= num
            res += result
        return (res/second_tup_num_sum)
