#!/usr/bin/python3

def no_c(my_string):
	new_str = [i for i in my_string if 'c' != i or 'C' != i]
	return ("".join(new_str))
