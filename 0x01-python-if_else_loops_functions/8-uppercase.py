#!/usr/bin/python3
def uppercase(string):
    for d in string:
        if ord(d) >= 97 and ord(d) <= 122:
            d = chr(ord(d) - 32)
            print("{}".format(d),end="")
    print()
