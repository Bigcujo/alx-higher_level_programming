#!/usr/bin/python3
""" prints the ASCII alphabet in reverse order. """

for i in range(122, 96, -1):
    print("{}".format(chr(i) if i % 2 == 0 else chr(i - 32)), end="")

