#!/usr/bin/python3
for alpha in range(97, 123):
    if alpha == 113 or alpha == 101:
        continue
    print("{:c}".format(alpha), end="")
