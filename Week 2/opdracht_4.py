binary_value = ""

"""
Description
	Recursive function to get the binary number from a decimal number

Parameters
----------
number	:	int
	The number of which you want the binary number
	
Return
------
binary_value : string
"""
def binary(number):
	assert a >= 0
	
	global binary_value

	if(number == 0):
		# binary_value = binary_value.join(reversed(binary_value))
		binary_value = binary_value[::-1]
		return binary_value

	binary_value = binary_value + str(number % 2)
	number = number // 2

	print("BNR: " + binary_value)
	print("Number: " + str(number))

	return binary(number)


a = 10
print(binary(a))