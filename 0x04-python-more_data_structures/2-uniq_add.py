#!/usr/bin/python3
def uniq_add(my_list=[]):

    unique_set = set(my_list)

    sum_unique = 0

    for num in unique_set:
        sum_unique += num
    return sum_unique

