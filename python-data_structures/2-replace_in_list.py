#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    if ux < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list

my_list = [1, 2, 3, 4]

print(replace_in_list(my_list, 2, 10))
print(replace_in_list(my_list, -1, 10))
print(replace_in_list(my_list, 10, 10))
