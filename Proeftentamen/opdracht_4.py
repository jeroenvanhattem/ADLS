class TreeNode:
	def __init__(self, data, left, right):
		self.data = data
		self.left = left
		self.right = right

def count(n, x):
	if n == None:
		return 0
	else:
		return (1 if (n.data	 == x) else 0) + count(n.left, x) + count(n.right, x)

n1 = TreeNode(1, None, None)
n2 = TreeNode(4, None, None)
n3 = TreeNode(3, None, None)
n4 = TreeNode(4, n1, None)
n5 = TreeNode(3, n2, None)
n6 = TreeNode(4, None, n3)
n7 = TreeNode(1, n4, n5)
n8 = TreeNode(5, None, n6)
n9 = TreeNode(4, n7, n8)
print(count(n9, 4))
print(count(n9, 3))
