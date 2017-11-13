"""
description
The getPrimes(a) function will search for all prime numbers under 1000 using the Sieve of Eratosthenes. These will be returned in a list. 
----------
a : list
A string containing all numbers from 2 up to 1000

Return
------
a: list
A list container all prime numbers under 1000
"""

array = list(range(2, 1001))

def getPrimes(a):
	for x in a:
		if x % 2 == 0:
			if x != 2:
				a.remove(x)
	for x in a:
		if x % 3 == 0:
			if x != 3:
				a.remove(x)
	for x in a:
		if x % 5 == 0:
			if x != 5:
				a.remove(x)
	for x in a:
		if x % 7 == 0:
			if x != 7:
				a.remove(x)
	for x in a:
		for y in a:
			if x != y:
				if y % x == 0:
					a.remove(y)
	return a

print(getPrimes(array)) 