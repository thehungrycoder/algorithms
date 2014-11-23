#!/usr/local/bin/python

# an implementation of O(N^2), exponential growth to the input size. 

import sys

def getWordsHavingChar(sentence, findChar):
	wordsContainingChar = []

	for word in sentence.split(' '):
		for char in list(word):
			if char is findChar:
				wordsContainingChar.append(word)
				break
			else:
				continue

	return wordsContainingChar


try:
	print getWordsHavingChar(sys.argv[1], sys.argv[2])
except IndexError:
	print "Insufficient inputs"

sys.exit(0)