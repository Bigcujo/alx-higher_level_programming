#!/usr/bin/python3
def no_c(m_strs):
    new_strs = ""
    for element in m_strs:
        if element != "c" and element != "C":
            new_strs += element
    return new_strs
