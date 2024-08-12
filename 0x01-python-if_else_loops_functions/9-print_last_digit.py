#!/usr/bin/python3
""" prints the last digit of a given int """


def print_last_digit(number):

	"""gives the last digit of the given number"""
last_int = abs(number) % 10
print(last_int, end='')
return last_int
