#!/usr/bin/python3
def magic_string():
    magic_string.count = getattr(magic_string, 'count', -1) + 1
    print("BestSchool, " * magic_string.count)
