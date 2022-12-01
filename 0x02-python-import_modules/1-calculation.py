#!/usr/bin/python3

if __name__ == "__main__":
	""" Do basic math calculations using custom module"""
	from calculator_1 import add, sub, mul, div

	a = 10
	b = 5
	
	""" sum two integer"""
	print("{} + {} = {}".format(a, b, add(a, b)))

	""" substract two integer"""
	print(f"{a} - {b} = {sub(a, b)}")

	""" multiply two integer"""
	print("{} * {} = {}".format(a, b, mul(a, b)))

	"""divid two integer"""
	print(f"{} / {} = {div(a, b)}")


