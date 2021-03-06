import string


# -----------------------------------------------------------------------------------------------------------------------------


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

array1 = [0, 10, 4, 6, 7, 12, 15]

def opdracht_1(a):
	if len(array) > 0:
		highest = a[0]
		for x in a:
			if x > highest:
				highest = x
		return highest
	else:
		return "Array is empty"



# -----------------------------------------------------------------------------------------------------------------------------


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

array2 = 'een123zin45 6met-632meerdere+7777getallen'

def opdracht_2(a):
	length = len(a)
	b =[]
	for x in a:
		if x.isdigit():
			b.append(x)
	return b


# -----------------------------------------------------------------------------------------------------------------------------



array3 = list(range(2, 1001))
"""
Decription
The modulo(a,b) function calculates a % b and returns the answer.

Parameters
----------
a : int
b : int

Return
------
answer: a
The modulo.
"""
def modulo(a, b):
	while a >= b:
		a = a - b
		# print(a)
		if(a == 0):
			return True
		elif ((a < b) and (a > 0)):
			return False
		# print(a)

"""
Description
The getPrimes(a) function will search for all prime numbers under 1000 using the Sieve of Eratosthenes. These will be returned in a list. 
----------
a : list
A string containing all numbers from 2 up to 1000

Return
------
a: list
A list container all prime numbers under 1000
"""

"""
2      3      5      7     11     13     17     19     23     29 
 31     37     41     43     47     53     59     61     67     71 
 73     79     83     89     97    101    103    107    109    113 
127    131    137    139    149    151    157    163    167    173 
179    181    191    193    197    199    211    223    227    229 
233    239    241    251    257    263    269    271    277    281 
283    293    307    311    313    317    331    337    347    349 
353    359    367    373    379    383    389    397    401    409 
419    421    431    433    439    443    449    457    461    463 
467    479    487    491    499    503    509    521    523    541 
547    557    563    569    571    577    587    593    599    601 
607    613    617    619    631    641    643    647    653    659 
661    673    677    683    691    701    709    719    727    733 
739    743    751    757    761    769    773    787    797    809 
811    821    823    827    829    839    853    857    859    863 
877    881    883    887    907    911    919    929    937    941 
947    953    967    971    977    983    991    997
"""
def opdracht_3(a):

	for x in a:
		if x != 2:
			if modulo(x, 2) == True:
				a.remove(x)
	for x in a:
		if x != 3:
			if modulo(x, 3) == True: 
				a.remove(x)
	for x in a:
		if x != 5:
			if modulo(x, 5) == True:
				a.remove(x)
	for x in a:
		if x != 7:
			if modulo(x, 7) == True:
				a.remove(x)
	for x in a:
		for y in a:
			if x != y:
				if modulo(y, x) == True:
				# if y % x == 0:
					a.remove(y)
	return a


# -----------------------------------------------------------------------------------------------------------------------------


def opdracht_4():
	count = 0

	for i in range(100):
		birthdays = []
		for i in range(23):
			birthdays.append(random.randint(1, 365))

		for x in range(len(birthdays)):
			for y in range(len(birthdays)):
				if x != y:
					if birthdays[x] == birthdays[y]:
						count += 1;


	return count


# -----------------------------------------------------------------------------------------------------------------------------

print(opdracht_1(array1)) 
print(opdracht_2(array2)) 
print(opdracht_3(array3)) 
print("Times: ", opdracht_4())

