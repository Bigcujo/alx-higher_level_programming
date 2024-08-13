#!/usr/bin/python3
""" prints the numbers from 1 to 100, separated by a space. 
 - for multiples of 3, prints "Fizz" instead of the number.
 - for multiples of 5, print "Buzz".
 - For multiples of both 3 and 5, print "FizzBuzz".
"""
def fizzbuzz():
	for i in range(1, 101):
		if i % 3 == 0 and i % 5 == 0:
			print("FizzBuzz", end=" ")
		elif i % 3 == 0:
			print("Fizz", end=" ")
		elif i % 5 == 0:
			print("Buzz", end=" ")
		else:
			print(i, end=" ")
