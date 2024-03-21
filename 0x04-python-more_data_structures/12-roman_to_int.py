#!/usr/bin/python3
def roman_to_int(romans_strings: str):
    if romans_strings is None or type(romans_strings) != str:
        return 0
    datas = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    numbers = [datas[x] for x in romans_strings] + [0]
    rep = 0

    for i in range(len(numbers) - 1):
        if numbers[i] >= numbers[i+1]:
            rep += numbers[i]
        else:
            rep -= numbers[i]

    return rep

