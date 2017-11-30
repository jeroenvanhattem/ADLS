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

	def at(self, n):
		if(len(self.stack_list) != 0):
			x = self.stack_list[n]
			return x
		else:
			return "Empty"

	def remove(self, x):
		self.stack_list.remove(x)

	def is_empty(self):
		if(len(self.stack_list) == 0):
			return True
		else: 
			return False


def check_brackets(x):
	brackets = stack()
	opening = ["{", "[", "("]
	closing = ["}", "]", ")"]

	for i in x:
		brackets.push(i)

	for i in range(len(x)):
		y = brackets.at(i)
		if(y in closing):
			if(brackets.at(i - 1) in opening):
				if(opening.index[i] == closing.index[i]):
					brackets.remove(brackets[i])
					brackets.remove(brackets[i])

print(check_brackets("{[(})]"))