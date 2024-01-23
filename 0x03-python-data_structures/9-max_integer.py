#!/usr/bin/python3
def max_integer(m_list=[]):
    new_list = []
    if m_list:
        m_list.sort(reverse=True)
        return (m_list[0])
    return (None)
