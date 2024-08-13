#!/usr/bin/python3
"""Creates a copy of the string, removing the character at the position of n."""

def remove_char_at(str, n):
    """Definition of the function."""
    if n < 0 or n >= len(str):
        return str  # If n is out of bounds, return the original string
    return str[:n] + str[n+1:]
