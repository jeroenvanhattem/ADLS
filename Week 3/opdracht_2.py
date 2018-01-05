class ListNode:
	def __init__(self,data,next):
		self.data = data
		self.next = next

	def __repr__(self):
		return str(self.data)

class MyCircularLinkedList:
	def __init__(self):
		self.tail = None

	def __repr__(self):
		s = ''
		if not self.tail:
			s = "Empty"
		else:
			current = self.tail
			while current.next != self.tail:
				s += str(current.data) + " -> "
				current = current.next
			s += str(current)
		return s

	def append(self, e):
		if not self.tail:
			self.tail = ListNode(e, None)
			self.tail.next = self.tail
		else:
			current = self.tail
			while current.next != self.tail:
				current = current.next

			x =ListNode(e, None)
			x.next = self.tail
			current.next = x
			self.tail = current.next

	def delete(self,e):
		if not self.tail:
			print("Can't delete node, list is empty")
		else:
			current = self.tail
			backup = None

			if current.next == self.tail:
				self.tail = None
			else:
				while current.data != e:
					if current.next == self.tail:
						print("Node not found")
					else:
						backup = current
						current = current.next

				if current == self.tail:
					backup = self.tail
					while backup.next != self.tail:
						backup = backup.next

					self.tail = self.tail.next
					backup.next = self.tail
				else:
					if current.next == self.tail:
						backup.next = self.tail
					else:
						backup.next = current.next

	

mylist = MyCircularLinkedList()
print(mylist)
mylist.append(1)
print(mylist)
mylist.append(2)
print(mylist)
mylist.append(3)
print(mylist)
mylist.delete(2)
print(mylist)
mylist.delete(1)
print(mylist)
mylist.delete(3)






































