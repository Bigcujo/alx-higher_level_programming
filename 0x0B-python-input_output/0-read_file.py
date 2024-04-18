#!/usr/bin/python3

"""Define a function thats reads an encrpyted file"""

def read_file(filename=""):
    """prints the content of a UTF8 type of file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
