#!/usr/bin/python3
def new_in_list(m_lists, idx, elements):
    if idx < 0:
        return m_lists
    elif idx >= len(m_lists):
        return m_lists
    new_lists = list(m_lists)
    new_lists[idx] = elements
    return new_lists
