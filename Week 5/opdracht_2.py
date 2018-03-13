import math
INFINITY = math.inf

def contains(full_list, check_list):
	"""
    The contains function sees if a list contains another list of elements

	Parameters
	----------
	full_list : list 
        The list that will be checked for the other list containing elements
	check_list : list
        The list with elements that must be in the other list

	Return
	------
	boolean
        All elements found in the list

	"""
	for e in check_list:
		if e not in full_list:
			return False

	return True
    
class myqueue(list):
	def __init__(self, a=[]):
		list.__init__(self, a)

	def dequeue(self):
		return self.pop(0)

	def enqueue(self, x):
		self.append(x)

class Vertex:
	def __init__(self, data):
		self.data = data

	def __repr__(self):
		return str(self.data)

	def __lt__(self, other):
		return self.data < other.data 


class graph:
	def __init__(self, G):
		self.G = G

	def vertices(self):
		return sorted(self.G)

	def edges(self):
		return [(u, v) for u in self.vertices() for v in self.G[u]]

	def reset(self):
		for v in self.vertices():
			k = [e for e in vars(v) if e != 'data']
			for e in k:
				delattr(v, e)

	def clear(self):
		self.G.clear()

class BFS:
	"""
    BFS algorithm class

	Parameters
	----------
	graph : graph
        This graph contains all the Vertexes
	root_vertex: Vertex
        The root node from the graph

	"""
	def __init__(self, graph, root_vertex):
		self.graph = graph
		self.root_vertex = root_vertex
		self.set_root(self.root_vertex)

	def set_root(self, s):
		V = self.graph.vertices()
		s.predecessor = None
		s.distance = 0
		for v in V:
			if v != s:
				v.distance = INFINITY
		q = myqueue()
		q.enqueue(s)
		while q:
			u = q.dequeue()
			for v in self.graph.G[u]:
				if v.distance == INFINITY:
					v.distance = u.distance + 1
					v.predecessor = u
					q.enqueue(v)

	def find_children(self, v):
		"""
        The find_children function is used to find the children or neighbours of a Vertex.

		Parameters
		----------
		v : Vertex
            The Vertex who's children we want to find.

		Return
		------
		children : Vertex array
            A list of the Vertex' children

		"""
		edges = self.graph.edges()
		children = []
		for edge in edges:
			if v == edge[0]:
				children.append(edge[1])
		return children

	def show(self):
		print('tree:', end=' ')
		for v in self.graph.vertices():
			print('(' + str(v), end='')
			if hasattr(v, 'distance'):
				print(',d:' + str(v.distance), end='')
			if hasattr(v, 'predecessor'):
				print(',p:' + str(v.predecessor), end='')
			print(')', end=' ')
		print()

	def show_path(self, u, v):
		self.set_root(u)
		a = []
		if hasattr(v, 'predecessor'):
			current = v
			while current:
				a.append(current)
				current = current.predecessor
			a.reverse()
		return a

	def show_sorted(self):
		print('sorted tree:')
		V = self.graph.vertices()
		V = [v for v in V if hasattr(v,'distance') and hasattr(v,'predecessor')]
		V.sort(key=lambda x: (x.distance, x.predecessor))
		d = 0
		for v in V:
			if v.distance > d:
				print()
				d += 1
			print('(' + str(v) + ',d:' + str(v.distance) + ',p:'
				  + str(v.predecessor), end='')
			print(')', end=' ')
		print()

	def no_cycles(self):
		"""
        The no_cycles function checks if there are cycles in the graph.

		Return
		------
		boolean:
			Return true if the graph contains no cycles.

		"""
		V = self.graph.vertices()

		for v in V:
			children = self.find_children(v)

			if len(children) > 1:
				for child in children:
					relatives = self.find_children(child)

					if len(relatives) > 1:
						relatives.append(child)
						family = children[:]
						family.append(v)

						if contains(relatives, family):
							return False

						del family[:]
					del relatives[:]
				del children[:]

		return True


v = [Vertex(i) for i in range(8)]

g = {
	 v[0]:[ v[4], v[5] ],
	 v[1]:[ v[4], v[5], v[6] ],
	 v[2]:[ v[4], v[5], v[6] ],
	 v[3]:[ v[7] ],
	 v[4]:[ v[0], v[1], v[2], v[5] ],
	 v[5]:[ v[0], v[1], v[2], v[4] ],
	 v[6]:[ v[1], v[2] ],
	 v[7]:[ v[3] ]
	 }

g2 = {
	 v[0]:[ v[4], v[5] ],
	 v[1]:[ v[4], v[6] ],
	 v[2]:[ v[5] ],
	 v[3]:[ v[7] ],
	 v[4]:[ v[0], v[1] ] ,
	 v[5]:[ v[0], v[2] ],
	 v[6]:[ v[1] ],
	 v[7]:[ v[3] ]
	 }

G = graph(g2)

B = BFS( G, v[1] )

print( "Are there no cycles : ", B.no_cycles() )

