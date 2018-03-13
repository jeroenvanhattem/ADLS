import string

"""
description
The getNumbers(a) function will seperate numbers from letters within a string. These numbers will be returned in a list.
----------
a : list
A string containing letters and numbers.

Return
------
b: list
A list that contains the extracted numbers from list A
"""

a = 'een123zin45 6met-632meerdere+7777getallen'

def getNumbers(a):
	length = len(a)
	b =[]
	for x in a:
		if x.isdigit():
			b.append(x)
	return b

print(getNumbers(a)) 