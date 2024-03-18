#!/usr/bin/python3
copy_list = __import__('19-copy_list').copy_list

my_list = [6, 8, 9]
print(my_list)

new_list = copy_list(my_list)

print(my_list)
print(new_list)

print(new_list == my_list)
print(new_list is my_list)
