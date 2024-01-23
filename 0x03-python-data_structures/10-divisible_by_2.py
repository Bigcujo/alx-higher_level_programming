#!/usr/bin/python3
def divisible_by_2(m_list=[]):
    new_lists = []
    if m_list:
        for num in m_list:
            new_lists.append(False if num % 2 else True)
        return new_lists
