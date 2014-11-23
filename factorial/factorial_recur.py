#!/usr/local/bin/python

import sys

try:
	num = int(sys.argv[1])
except IndexError:
	sys.exit("You must provide the number you want the num of!")
except ValueError:
	sys.exit("Not a valid number")

if num < 1:
	sys.exit('0')

def fact(num):
	if num > 1:
		return num * fact(num - 1)
	else:
		return num

print "Factorial of %d is %d" % (num, fact(num))
sys.exit(0)