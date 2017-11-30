def machtv1(a,n):
	return a**n

def machtv2(a,n):
	assert n > 0
	m = 1
	for _ in range(0,n):
		m = m * a

	return m

def machtv3(a, n):
	assert n > 0

	x = a
	counter = 0

	m = 1
	while n > 0:
		if n % 2 == 0:
			x = (x * a)
			n = n / 2
		else:
			x = (x * a)
			n = n - 1
			counter = counter + 1
	print("Counter: ", counter)
	return "Resultaat: ", x

print(machtv3(3,10000))