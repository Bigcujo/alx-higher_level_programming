#!/usr/bin/python3
""" returns a to the power of b """

def pow(a, b):
	"""
	Computes a to the power of b and returns the result.
	
	"""

	result = 1
	if b == 0:
		return 1
	elif b > 0:
		for i in range(b):
			result *= a
	else:
		for i in range(-b):
			result /= a
	return result
