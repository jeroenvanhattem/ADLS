import random

class HashStorage:
	"""
	Definition
		Initialize storage
	"""
	def __init__(self):
		self.hashDict = {}
		self.hashDuplicate = []

class EqualHashValues:
	"""
	Definition
		Initializing storage
	"""
	def __init__(self):
		self.storage = HashStorage()

	"""
	Definition
		The way it will be printed
	"""
	def __repr__(self):
		s = ""
		s += "Same hash found:\n"
		for duplicates in self.storage.hashDuplicate:
			s += self.listToString(duplicates) + "\n"

		return s
		
	"""
	Definition
		Convert to string

	Return
	------
	value : string
		The converted string
	"""
	def listToString(self, list):
		s = "<"
		m = " , ".join(map(str, list))
		return s + m + ">"

	
	"""
	Definition
		Find duplicates
	
	"""
	def findDuplicate(self):
		while True:
			value = random.uniform(0.1, 1.0)
			key = hash( value ) & 0xffffffff

			if key in self.storage.hashDict:
				break

			self.storage.hashDict.update({key: value})

		self.storage.hashDuplicate.append(
			[self.storage.hashDict.get(key),
			 value]
		)

	"""
	Definition
		Find duplicated within the first N items
	
	Parameters
	----------
	N : int
		The amount of times to check for duplicates
	"""
	def findNDuplicates(self, N):
		for i in range(N):
			self.findDuplicate()


test = EqualHashValues()
test.findNDuplicates( 5 )

print(test)

