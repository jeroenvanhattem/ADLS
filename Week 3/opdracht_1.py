def check(a,i): # ga na of i aan a toegevoegd kan worden
	n = len(a)
	return not (i in a or
		 # niet in dezelfde kolom
		 i+n in [a[j]+j for j in range(n)] or
		 # niet op dezelfde diagonaal
		 i-n in [a[j]-j for j in range(n)])
		# niet op dezelfde diagonaal

def printQueens(a):
	n = len(a)
	for i in range(n):
		for j in range(n):
			if a[i] == j:
				print("X",end= " ")
			else:
				print("*",end= " ")
		print()
	print()

def rsearch(column):

	global N
	a.append(column)

	if len(a) == N:
		return True

	for i in range(N):
		if check(a,i) and rsearch(i):
			return True

	del a[-1]
	return False





def rsearch_all(N):
	# global solutions

	for i in range(N):
		if rsearch(i):
			print("Oplossing: ", i + 1)
			printQueens(a)
		del a[:]


a = [] # a geeft voor iedere rij de kolompositie aan
solutions = []
t = 0
N = 8

rsearch_all(N)