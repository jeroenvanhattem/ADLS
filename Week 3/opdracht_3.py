class BinarySearchNode:
	def __init__(self, element = None, left = None, right = None):
		self.element = element
		self.left = left
		self.right = right

	def __repr__(self,nspaces=0):
		s1 = ''
		if self.right:
			s1 = self.right.__repr__(nspaces + 3)
		s2 = ' '*nspaces + str(self.element) + '\n'
		s3 = ''
		if self.left:
			s3 = self.left.__repr__(nspaces + 3)
		return s1 + s2 + s3

	def size(self):
		s = 1
		if self.left:
			s += self.left.size()
		if self.right:
			 s += self.right.size()
		return s

	def rsearch(self, e, i):
		current = self
		found = False
		
		if not found and current:
			if current.element < e:
				current = current.right
			elif current.element > e:
				current = current.left
			else:
				found = True

		if i == 0 and not found:
			return "Not found"

		if found:
			return current

		else:
			current.element = current.element + 1
			print(current)
			return self.rsearch(e, i - 1)

	def max(self):
		current = self

		highest = current

		while current:
			highest = current.left

		return highest



	def rinsert(self, e):
		parent = self
		current = None
		found = False

		if parent.element < e:
			current = parent.right
		elif parent.element > e:
			current = parent.left
		else :
			found = True

		while not found and current:
			parent = current
			if parent.element < e:
				current = parent.right
			elif parent.element > e:
				current = parent.left
			else:
				found = True

		if not found:
			if parent.element < e:
				parent.right = BinarySearchNode(e, None, None)
			else:
				parent.left = BinarySearchNode(e, None, None)
			return not found

class BinarySearchTree:
	def  __init__(self, root = None):
		self.root = root

	def __repr__(self):
		if self.root:
			return str(self.root)
		else:
			return 'null-tree'

	def size(self):
		if self.root:
			return self.root.size()
		else:
			return 0

	def max(self):
		if self.root:
			return self.root.max()
		else:
			print("self.root == false")
		
	def rsearch(self, e, i):
		if self.root and e:
			return self.root.rsearch(e, i)
		else:
			return None

	def rinsert(self, e):
		if e:
			if self.root:
				return self.root.rinsert(e)
			else:
				self.root = BinarySearchNode(e, None, None)
				return True
		return False

	def showLevelOrder(self):
		print("stuff")


myTree = BinarySearchTree()

myTree.rinsert(6)
myTree.rinsert(5)
myTree.rinsert(9)
myTree.rinsert(8)
myTree.rinsert(2)
myTree.rinsert(7)
myTree.rinsert(1)
myTree.rinsert(4)
myTree.rinsert(3)
# print(myTree.rsearch(4, myTree.size()))
print(myTree.max())
# print(myTree)
# myTree.showLevelOrder()