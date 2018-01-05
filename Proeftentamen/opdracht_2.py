def rec_identical_elements(a):
	if len(a) == 1:
		return True

	if a[0] == a[1]:
		return rec_identical_elements(a[1:])
	
	return False

a = ["a", "a", "a", "a", "a", "b"]

print(rec_identical_elements(a))