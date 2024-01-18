#!/usr/bin/python3
for first in range(0, 10):
    for second in range(first + 1, 10):
        if first == 8 and second == 9:
            print(89)
        elif first < 9 and second <= 9:
            print("{:d}{:d}".format(first, second), end= ", ")
