import math

def machtv1(a,n):
	return a**n

def machtv2(a,n):
	assert n > 0
	m = 1
	for _ in range(0,n):
		m = m * a

	return m

"""
Description
The machtv3(a) function calculates powers according to log(n)

Parameters
----------
a : base
n : power

Return
------
result: int
	The result : a^n
"""
def machtv3(a, n):
	assert n > 0
	result = 1
	while n > 0:
		if n % 2 == 0:
			n = n // 2
			a = a ** 2
		else:
			n-=1
			result *= a
	return result

n = 10000
print(machtv3(2,n))
print(str(n) + " -> " + str(math.log(n)) + " multiplications")