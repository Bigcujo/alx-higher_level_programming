#!/usr/bin/python3
"""Finds the peak value in an unsorted list"""

def find_peak(list_of_integers):
    """Finds the peak value in the passed list_of_integers"""

    if list_of_integers is None or list_of_integers ==[]:
        return None
    lowestInt = 0
    highestInt = len(list_of_integers)
    midInt = ((highestInt - lowestInt) // 2) + lowestInt
    midInt = int(midInt)
    if highestInt == 1:
        return list_of_integers[0]
    if highestInt == 2:
        return max(list_of_integers)
    if list_of_integers[midInt] >= list_of_integers[midInt - 1] and\
            list_of_integers[midInt] >= list_of_integers[midInt + 1]:
                return list_of_integers[midInt]
    if midInt > 0 and list_of_integers[midInt] < list_of_integers[midInt + 1]:
        return find_peak(list_of_integers[midInt:])
    if midInt > 0 and list_of_integers[midInt] < list_of_integers[midInt - 1]:
        return find_peak(list_of_integers[:midInt])
