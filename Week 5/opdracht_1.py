import math

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

class Vertex:
	def __init__(self, data):
		self.data = data

	def __repr__(self):
		return str(self.data)

	def __lt__(self, other):
		return self.data < other.data 

class BFS:
	def is_connected(self, G, s):	# G is de graaf, s is de root-node
		V = self.vertices(G)
		s.predecessor = None
		s.distance = 0

		for v in V:
			if v!= s:	# Is de huidige node niet de root?
				v.distance = math.inf
		q = stack()
		q.push(s)
		while q:
			u = q.pop()
			for v in G[u]:
				if v.distance == math.inf:
					v.distance = u.distance + 1
					v.predecessor = u
					q.push(v)
			print(v)
		# return True

	def vertices(self, G):
		return sorted(G)		

	def edges(self, G):
		return [(u,v) for u in self.vertices(G) for v in G[u]]

v = [Vertex(i) for i in range(5)]

G = { v[0]:[v[1],v[4]],
  	  v[1]:[v[0],v[2],v[3],v[4]],
  	  v[2]:[v[1],v[3]],
	  v[3]:[v[1],v[2],v[4]],
	  v[4]:[v[0],v[1],v[3]]
	 }

graaf = BFS()

print("Vertices(G): ", graaf.vertices(G))
print("Edges(G): ", graaf.edges(G))

# if(graaf.is_connected(G, v[1])):
print(graaf.is_connected(G, v[0]))
print(graaf.is_connected(G, v[1]))
print(graaf.is_connected(G, v[2]))
	# print("Graaf is verbonden")
# else:
# 	print("Graaf is niet verbonden")