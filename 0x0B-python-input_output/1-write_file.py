#!/usr/bin/python3
"""Define a function that writes to a file and returns the num of charaters."""

def write_file(filename="", text=""):
    """write a string to a UTF8 text file.

    Args:
    filename(str): the name of the file i want to write to.
    text(str): the text to write to the file we are opening.
    Returns:
    the number of characters written.
    """

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
