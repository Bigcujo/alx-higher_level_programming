#!/usr/bin/python3
def delete_at(cujo_list=[], idx=0):
    if idx < 0:
        return cujo_list
    elif idx >= len(cujo_list):
        return cujo_list
    del cujo_list[idx]
    return cujo_list
