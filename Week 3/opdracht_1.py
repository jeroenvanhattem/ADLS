"""
Description
	Find a solution to the problem

Parameters
----------
column : int
	The location in the first row on which the queen will be located.

Return
------
bool
	Return True when there will be no interference with other queens
"""
def check(a,i):
	n = len(a)
	return not (i in a or
		 i+n in [a[j]+j for j in range(n)] or
		 i-n in [a[j]-j for j in range(n)])


"""
Description
	Print te board

Parameters
----------
a : list
	The chessboard with the queens

"""
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


"""
Description
	Find a solution to the problem

Parameters
----------
column : int
	The location in the first row on which the queen will be located.
"""

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

"""
Description
	Call the rsearch() function for every a[i]

Parameters
----------
N : int
	The amount of wanted solutions
"""

def rsearch_all(N):
	# global solutions

	for i in range(N):
		if rsearch(i):
			print("Solution: ", i + 1)
			printQueens(a)
		del a[:]


a = []
solutions = []
t = 0
N = 8

rsearch_all(N)