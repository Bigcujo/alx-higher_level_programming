#!/usr/bin/python3
def print_reversed_list_integer(m_list=[]):
    if m_list:
        for elements in m_list[::-1]:
            print("{:d}".format(elements))
