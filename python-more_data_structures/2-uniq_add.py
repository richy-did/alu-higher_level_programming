#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_number = set(my_list)
    total = 0
    for num in unique_number:
        total += num
        return total
