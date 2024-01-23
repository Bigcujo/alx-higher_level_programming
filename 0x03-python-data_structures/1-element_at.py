#!/usr/bin/python3
def element_at(my_lists, idx):
    if idx < 0:
        return None
    elif idx >= len(my_lists):
        return None
    return my_lists[idx]

