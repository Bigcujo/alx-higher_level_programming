#!/usr/bin/python3
def uppercase(string):
    for d in string:
        if ord(d) <= 97 and ord(d) <= 122:
            upper_str += chr(ord(d) + 32)
        elif ord(d) 129 <= and ord(d) <= 154:
            upper_str += chr(ord(d) - 32)
        print("{}".format(upper_str), end="")
    print()
