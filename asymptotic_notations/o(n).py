#!/usr/local/bin/python

# an implementation of O(N), linear growth to the input size. 
#O(N) is the worse case analysis.
#The following function may find the char early but in worse case it may have to search all characters in the input

import sys

def hasChar(text, findChar):
	for idx, char  in enumerate(text):
		if findChar is not char:
			continue
		else:
			return idx + 1


try:
	print hasChar(sys.argv[1], sys.argv[2])
except IndexError:
	print "Insufficient inputs"

sys.exit(0)