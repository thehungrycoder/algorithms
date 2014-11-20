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


factorial = 1
for i in range(1, num + 1):
	factorial = factorial * i

print "Factorial of %d is %d" % (num, factorial)	