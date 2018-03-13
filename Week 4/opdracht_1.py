import random

class hashSet:
	"""
	Definition
		Initialize the hashSet
	"""
	def __init__(self, value):
		self.element = set([value])

	"""
	Definition
		How will the Set be printed
	
	Return
	------
	value : list
		The Set will be returned as a list: [key, value]
	"""
	def __str__(self):
		s = "["
		m = ",".join( map(str, self.element) )
		return s + m + "]"

class hashTable:
	"""
	Definition
		Initialize the hashtable
	
	Parameters
	----------
	size : int
		The size of the hashtable
	"""
	def __init__(self, size=16):
		self.size = size
		self.item_counter = 0
		self.table = [None] * size

	"""
	Definition
		Print the hashtable
	"""
	def printTable(self):
		s = ""
		for i in self.table:
			if i is not None:
				s += str(i) + "\n"
		print( "Table (size = ", self.size, ")" )
		print( s )
		
	"""
	Definition
		Get the index of a key
	
	Parameters
	----------
	key : int
		The key you want the index from

	Return
	------
	index : int
		Get the index of a key
	"""
	def index(self, key):
		return hash(key) % self.size
	
	"""
	Definition
		Check whether the table is empty or not
	
	Return
	------
	value : bool
		1 if empty, 0 if not
	"""
	def setEmpty(self, set):
		return len(set) == 0
	
	"""
	Definition
		Calculate how full the table is

	Return
	------
	size : int
	"""
	def getLoadFactor(self):
		return self.size * 0.75
	
	"""
	Definition
		Double the size
	"""
	def doubleSize(self):
		self.size *= 2
		
	"""
	Definition
		Search in the table for a key
	
	Parameters
	----------
	e : item
		To be found key

	Return
	------
	e : item
		Return the item if found, return -1 if not found
	"""
	def search(self, e):
		index = self.index(e)
		if self.table[index] != None:
			set = self.table[index].element
			if e in set:
				return e
		else:
			return -1
		
	"""
	Definition
		Insert an item
	
	Parameters
	----------
	e : item
		Add this item to the Hashtable
	"""
	def insert(self, e):
		index = self.index(e)
		if self.table[index] == None:
			self.table[index] = HashSet(e)
			self.item_counter += 1
		else:
			set = self.table[index].element
			set.add(e)
			self.item_counter += 1

		if self.item_counter > self.getLoadFactor():
			self.rehash()

	"""
	Definition
		Delete this item from the Hashtable
	
	Parameters
	----------
	e : item
		The to be deleted item

	Return
	------
	element : item
		The deleted item
	"""
	def delete(self, e):
		element = self.search(e)
		if element != -1:
			index = self.index(e)
			set = self.table[index].element
			set.remove(e)

			if self.setEmpty(set):
				self.item_counter -= 1
				self.table[index] = None

		return element
	
	
	"""
	Definition
		Rehash the table
	"""
	def rehash(self):
		temp_table = self.table

		self.doubleSize()
		self.item_counter = 0
		self.table = [None] * self.size

		for set in temp_table:
			if set is not None:
				for item in set.element:
					self.insert(item)

		self.printTable()


def test_float():
	to_be_deleted = []
	t1 = HashTable()
	for _ in range(200):
		random_num = random.uniform(0.1, 1.0)
		to_be_deleted.append(random_num)
		t1.insert(random_num)

	for i in to_be_deleted[0:100]:
		t1.delete(i)

def test_int():
	to_be_deleted = []
	t2 = HashTable()
	for _ in range(200):
		random_num = random.randrange(1, 100)
		to_be_deleted.append(random_num)
		t2.insert(random_num)

	for i in to_be_deleted[0:100]:
		t2.delete(i)

test_float()
#test_int()