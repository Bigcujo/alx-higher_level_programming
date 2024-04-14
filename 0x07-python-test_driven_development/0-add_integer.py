#!/usr/bin/python3

"""Defines an integer addition function."""


def add_integer(a, b=98):
    """Return the type casted result of b + a.
    Float arguments are typecasted to ints before addition is performed.
    Raises:
        TypeError: it will arise if a or b are not float or integers.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
