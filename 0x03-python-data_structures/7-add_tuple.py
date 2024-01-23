#!/usr/bin/python3
def add_tuple(tuples_a=(), tuples_b=()):
    len_a, len_b = len(tuples_a), len(tuples_b)
    new_tuples = ((tuples_a[0] if len_a >= 1 else 0) +
                 (tuples_b[0] if len_b >= 1 else 0),
                 (tuples_a[1] if len_a >= 2 else 0) +
                 (tuples_b[1] if len_b >= 2 else 0))
    return new_tuples
