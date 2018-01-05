def identical_elements(a):
	for i in a:
		if i != a[0]:
			return False
	return True


a = ["a", "a", "a", "a", "a", "b"]

print(identical_elements(a))