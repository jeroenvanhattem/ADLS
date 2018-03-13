class stack:
	"""
	Description
	Initialize the stack by creating an empty list.
	"""
	def __init__(self):
		self.stack_list = []

	"""
	Description
	Push the given parameter to the end of the stack

	Parameters
	----------
	x : list / int / char
	This can be whatever works
	"""
	def push(self, x):
		self.stack_list.append(x)

	"""
	Description
	Return the item on the end of the stack and remove it from the stack.

	Return
	------
	x: item
	The last item on the stack
	"""
	def pop(self):
		if(len(self.stack_list) != 0):
			x = self.stack_list[len(self.stack_list) - 1]
			self.stack_list.remove(x)
			return x
		else:
			return "Empty"

	"""
	Description
	Return the last item on the stack, without removing it.

	Return
	------
	x: item
	The last item on the stack
	"""
	def peek(self):
		if(len(self.stack_list) != 0):
			x = self.stack_list[len(self.stack_list) - 1]
			return x
		else:
			return "Empty"

	"""
	Description
	See if the stack is empty

	Return
	------
	bool 
	True if the stack is empty, False if it isn't
	"""
	def is_empty(self):
		if(len(self.stack_list) == 0):
			return True
		else: 
			return False

my_stack = stack()

my_stack.push(3)
print(my_stack.peek())
print(my_stack.pop())
my_stack.push(8)
print(my_stack.peek())