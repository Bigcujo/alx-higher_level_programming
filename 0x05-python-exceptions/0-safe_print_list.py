#!/usr/bin/python3

def safe_print_list(my_list=[], x):

    num = 0

    for r in range(x):
        try:
            print(my_list[r], end="")

            num += 1
        except IndexError:
            break
        print("")
        return num

