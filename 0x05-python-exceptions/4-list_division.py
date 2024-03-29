#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div_list = []

    index = 0
    quotient = 0
    while (index < list_length):
        try:
            if (isinstance(my_list_1[index], int) and
                    isinstance(my_list_2[index], int)):
                quotient = int(my_list_1[index]) / int(my_list_2[index])
            else:
                quotient = 0
                print("wrong type")
        except ZeroDivisionError:
            quotient = 0
            print("division by 0")
        except IndexError:
            quotient = 0
            print("out of range")
        finally:
            div_list.append(quotient)
        index += 1
    return (div_list)
