#!/usr/bin/python3
def print_matrix_integer(matris=[[]]):
    if not matris:
        print()
    else:
        for rows in range(len(matris)):
            for item in range(len(matris[rows])):
                if item != len(matris[rows]) - 1:
                    endspace = ' '
                else:
                    endspace = ''
                print("{:d}".format(matris[rows][item]), end=endspace)
            print()
