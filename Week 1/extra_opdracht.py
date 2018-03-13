"""
The conway(x) function counts the numbers according to the Look-and-say sequence

Parameters
----------
x : list
List container numbers

Return
------
counted: list
A list containing the amount of numbers, followed by the counted number. E.g. (3, 3) would return (2, 3), because there are two three's
"""

def conway(x):
	counted = []
	
	if not len(x):
		return "Length is zero"

	count = 0
	last = x[0]
	for n in range(len(x)):
		if x[n] == last:
			count += 1
			last = x[n]
		else:
			counted.append("[" + str(count) + "," + str(last) + "]")
			count = 1
			last = x[n]
		if n == len(x) - 1:
			counted.append("[" + str(count) + "," + str(last) + "]")
			return counted

x = [3, 3, 3, 3, 4, 4, 4, 5, 6, 6, 6, 6, 6, 7]
# 2,3  3,4  1,5  5,6
print(conway(x))