#!/usr/bin/python3
from sys import argv

argc = len(argv) - 1
plural = 's' if argc != 1 else ''
colon = ':' if argc != 0 else '.'

print("{} argument{}{}{}".format(argc, plural, colon, '\n' if argc else ''))

for i in range(1, argc + 1):
        print("{}: {}".format(i, argv[i]))
