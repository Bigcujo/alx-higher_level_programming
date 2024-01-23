#!/usr/bin/python3
def replace_in_list(m_list, idx, elements):
    if idx < 0:
        return m_list
    if idx >= len(m_list):
        return m_list
    m_list[idx] = elements
    return m_list
