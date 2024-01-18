#!/usr/bin/python3
for num1 in range (100):
    if num1 < 99:
        print("{:02d}, ".format(num1), end="")
    else:
        print("{:02d}".format(num1))
