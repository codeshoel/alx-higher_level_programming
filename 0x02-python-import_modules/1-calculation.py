#!/usr/bin/python3

if __name__ == "__main__":
	""" Do basic math calculations sum, difference, product and quotient of 10 and 5"""
	from calculator_1 import add, sub, mul, div

	a = 10
	b = 5
	
	""" sum of 10 and 5"""
	print("{} + {} = {}".format(a, b, add(a, b)), "\n")

	""" difference of 10 and 5"""
	print("{} - {} = {}\n".format(a, b, sub(a, b)), "\n")

	""" product of 10 and 5"""
	print("{} * {} = {}\n".format(a, b, mul(a, b)), "\n")

	"""quotient of 10 and 5"""
	print("{} / {} = {}\n".format(a, b, div(a, b)), "\n")


