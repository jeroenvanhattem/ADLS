import random

class hashSet:
	def __init__(self, value):
		self.element = set([value])

	def __str__(self):
		s = "["
		m = ",".join(map(str, self.element))
		return s + m + "]"

class hashTable:
	