#!/usr/bin/python3
def best_score(my_diction):
    return max(my_diction, key=my_diction.get) if my_diction else None
