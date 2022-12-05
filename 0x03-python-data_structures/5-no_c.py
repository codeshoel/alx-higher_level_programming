#!/usr/bin/python3

def no_c(my_string):
	if 'c' in my_string:
		new_string = my_string.remove('c')
		return new_string
	return my_string
