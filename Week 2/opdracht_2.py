class stack:
	def __init__(self):
		self.stack_list = []

	def push(self, x):
		self.stack_list.append(x)

	def pop(self):
		if(len(self.stack_list) != 0):
			x = self.stack_list[len(self.stack_list) - 1]
			self.stack_list.remove(x)
			return x
		else:
			return "Empty"

	def peek(self):
		if(len(self.stack_list) != 0):
			x = self.stack_list[len(self.stack_list) - 1]
			return x
		else:
			return "Empty"

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