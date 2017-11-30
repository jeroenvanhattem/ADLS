binary_value = ""

def binary(a):
	assert a >= 0
	
	global binary_value

	number = a

	if(number == 1):
		return binary_value

	binary_value = binary_value + str(number % 2)
	print("BNR: " + binary_value)
	number = number // 2
	print("Number: " + str(number))
	return binary(number)


a = 11
print(binary(a))