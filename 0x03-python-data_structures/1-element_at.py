#!/usr/bin/python3

def element_at(mylist, idx):
	if idx < 0:
		return None
	if idx > range(mylist):
		return None
	else:
		print("Element at index {:d} is {}".format(idx, element_at(mylist, idx)))
