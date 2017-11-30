def swap(a,i,j):
	a[i],a[j] = a[j],a[i]

import random

def qsort(a,low=0,high=-1):
	if high == -1:
		high = len(a) -1
	if low < high:
		swap(a,low, random.randint(low,high))
		m = low
		for j in range(low+1,high+1):
			if a[j] < a[low]:
				m += 1
				swap(a,m,j)
				swap(a,low,m)
			if m > 0:
				qsort(a,low,m-1)
	return a

a = [6, 4, 8, 6, 4, 64, 75, 234, 43,5, -2, -20]

print(qsort(a))