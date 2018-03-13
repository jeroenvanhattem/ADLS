import random
import math

"""
Description
	Swap function to swap two items

Parameters
----------
a	:	list
	The list which contains the to be swapped items
i	:	item
	To be swapped item
j	:	item
	To be swapped item
"""

def swap(a,i,j):
	a[i],a[j] = a[j],a[i]

"""
def qsort_1(a,low=0,high=-1)
Description
	A quicksort function to quickly sort an array

Parameters
----------
number	:	int
	The number of which you want the binary number
	
Return
------
counter1 : int
	How often items have been compared to each other
"""

def qsort_1(a,low=0,high=-1):
	global counter_1
	if high == -1:
		high = len(a) - 1
	if low < high:
		swap(a, low, random.randint(low, high))
		m = low
		for j in range(low + 1, high + 1):
			if a[j] < a[low]:
				m += 1
				swap(a, m, j)
		swap(a, low, m)
		if m > 0:
			counter_1 += 1
			qsort_1(a, low, m - 1)
			qsort_1(a, m + 1, high)
	return counter_1

"""
def qsort_2(a,low=0,high=-1)
Description
	A quicksort function to quickly sort an array

Parameters
----------
number	:	int
	The number of which you want the binary number
	
Return
------
counter2 : int
	How often items have been compared to each other
"""

def qsort_2(a,low=0,high=-1):
	global counter_2
	if high == -1:
		high = len(a) -1
	if low < high:
		swap(a,low, a.index(min(a)))
		m = low
		for j in range(low+1,high+1):
			if a[j] < a[low]:
				m += 1
				swap(a,m,j) # low < i <= m : a[i] < a[low] # i > m : a[i] >= a[low]
				swap(a,low,m) # low <= i < m : a[i] < a[m] # i > m : a[i] >= a[m]
		if m > 0:
			counter_2 += 1
			qsort_2(a,low,m-1)
			qsort_2(a,m+1,high)

	tmp = a[0]
	a[0] = a[-1]
	a[-1] = tmp
	return counter_2

a = []
b = []

for i in range (10000) :
	a.append(10000 - i)
	b.append(10000 - i)

counter_1 = 0
counter_2 = 0

print("qsort_1() -> Count: ", qsort_1(a,0,9999))
print("qsort_2() -> Count: ", qsort_2(b,0,9999))