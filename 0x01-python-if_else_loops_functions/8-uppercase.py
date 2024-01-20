#!/usr/bin/python3
def uppercase(string):
    upper_str = ""
    for d in string:
        if 'a' <=  d <= 'z':
            upper_str += chr(ord(d) - 32)
        else:
            upper_str += d
    print("{}".format(upper_str), end="")
    print()
