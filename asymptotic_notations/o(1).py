#!/usr/local/bin/python

# an implementation of O(1), constant time regardless of the length of the input (text)
import sys

def isFirstCharVowel(text):
	return text[0] in ['a', 'e', 'i', 'o', 'u']

try:
	print isFirstCharVowel(sys.argv[1])
except IndexError:
	print None

sys.exit(0)