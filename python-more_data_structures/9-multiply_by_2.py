#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_value = {}
    for num in a_dictionary:
        new_value[num] = a_dictionary[num] * 2 
    return new_value 
