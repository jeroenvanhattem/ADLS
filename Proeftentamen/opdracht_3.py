class ListNode:
	def __init__(self, data, next_node):
		self.data = data
		self.next = next_node

def contains_none_data_node(n):
	while n.next:
		if n.next.data == None:
			return True
		n = n.next

	else:
		return False

f = ListNode(None, None)
e = ListNode("data", f)
d = ListNode("data", e)
c = ListNode("data", d)
b = ListNode("data", c)
a = ListNode("data", b)

n = ListNode(1,ListNode(2,ListNode(3,None)))
print(contains_none_data_node(a))
# n = ListNode(1,ListNode(None,ListNode(3,None)))
# print(contains_none_data_node(n))
