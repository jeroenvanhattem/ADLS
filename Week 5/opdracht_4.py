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

	def get(self):
		return self.G

	def set(self, G):
		self.G = G

class BFS:
	"""
    BFS algorithm class

	Parameters
	----------
	graph : graph
        This graph contains all the vertices
	root_vertex: Vertex
        The root node from the graph

	"""
	def __init__(self, graph, vertex, root_node):
		self.graph = graph
		self.vertex = vertex
		self.root_node = root_node
		self.set_root(self.root_node)


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
		print('Sorted tree:')
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

	def connected_to_all(self, root_node):
		"""
        This function check if a Vertex is connected to every other vertex in the graph
        
		Parameters
		----------
		root_node : Vertex
            The Vertex we use to check

		Return
		------
		boolean:
			Return true if the Vertex is connected to every other vertex

		"""
		V = self.graph.vertices()
		for v in V:
			if v not in self.show_path(root_node, v):
				return False
		return True

	def inverted_graph(self):
		"""
        The inverted_graph functions return an inverted copy of the graph

		Return
		------
		graph : graph
            The inverted graph

		"""
		temp_graph = self.graph
		mirrored_graph = { i:[] for i in self.graph.vertices() }
		edges = temp_graph.edges()
		mirrored_edges = [(t[1], t[0]) for t in edges]

		for edge in mirrored_edges:
			mirrored_graph[ edge[0] ].append( edge[1] )

		return graph( mirrored_graph )

	def is_strongly_connected(self):
		"""
        The is_strongly_connected functions checks if a graph is strongly connected

		Return
		------
		boolean :
            Return true if the graph is strongly connected

		"""
		start_node = self.root_node
		if self.connected_to_all(start_node):
			mirrored = BFS(self.inverted_graph(), self.vertex[:], start_node)
			if mirrored.connected_to_all(start_node):
				return True

		return False

v = [Vertex(i) for i in range(3)]

g = {
	 v[0]:[ v[1] ],
	 v[1]:[ v[2] ],
	 v[2]:[ v[0] ],
	 }

g2 = {
	 v[0]:[ v[1] ],
	 v[1]:[ ],
	 v[2]:[ v[0], v[1] ],
	 }


G = graph(g)

B = BFS( G, v, v[0])

print( B.is_strongly_connected() )