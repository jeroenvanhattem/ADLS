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
	def is_connected(self, G, s):
		V = self.vertices(G)
		s.predecessor = None
		s.distance = 0

		for v in V:
			if v!= s:
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

graph = BFS()

print("Vertices(G): ", graph.vertices(G))
print("Edges(G): ", graph.edges(G))

print(graph.is_connected(G, v[0]))
print(graph.is_connected(G, v[1]))
print(graph.is_connected(G, v[2]))