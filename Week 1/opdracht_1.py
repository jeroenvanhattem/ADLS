"""
The myMax(a) function returns the highest number from a list passed as parameter.
Parameters
----------
a : list
List container numbers
Return
------
highest: int
The highest number from the list passed in the parameter.
"""

array = [0, 10, 4, 6, 7, 12, 15]

def myMax(a):
	if len(array) > 0:
		highest = a[0]
		for x in a:
			if x > highest:
				highest = x
		return highest
	else:
		return "Array is empty"

print(myMax(array)) 