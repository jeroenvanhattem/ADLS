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
        
	def add_node(self, list, value):
		list.append(value)
		new_edge = self.sort_nodes(list)
		return new_edge

	def remove_edge(self, e):
		graph = self.G

		u = e[0]
		value = e[1]

		edge = graph.get(u)
		if value in edge: edge.remove(value)

	def add_edge(self, e):
		graph = self.G

		u = e[0]
		value = e[1]

		edge = graph.get(u)
		new_edge = self.add_node(edge, value)
		graph.update({u: new_edge})

	def sort_nodes(self, row):
		size = len(row)

		for i in range(size):
			for j in range(size-1-i):
				if row[j] > row[j+1]:
					row[j], row[j + 1] = row[j + 1], row[j]

		return row

	def len_edges(self):
		"""
		The len_edges function counts the edges

		Return
		------
		i : int
            Amount of edges

		"""
		E = self.edges()
		i = 0
		for e in E:
			i += 1

		return i

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

	def find_children(self, v):
		edges = self.graph.edges()
		children = []
		for edge in edges:
			if v == edge[0]:
				children.append(edge[1])
		return children

	def get_bridges(self):
		bridges = []
		E = self.graph.edges()

		for u, v in E:
			self.graph.remove_edge( (u, v) )
			self.graph.remove_edge( (v, u) )
			path = self.show_path( v, u )

			if v not in path:
				bridges.append( (u,v) )
				bridges.append( (v,u) )

			self.graph.add_edge( ( u, v) )
			self.graph.add_edge( (v, u) )

		return sorted( list( set(bridges) ) )

	def is_bridge(self, edge):
		"""
        This function checks if an edge is a bridge

		Parameters
		----------
		edge : edge
            The edge to be check

		Return
		------
		boolean:
            Return True if the edge is a bridge

		"""
		bridges = self.get_bridges()
		if edge in bridges:
			return True

		return False

	def is_euler_graph(self):
		"""
        The is_euler_graph function checks if a graph is an Eular path

		Return
		------
		boolean:
			Return True is the graph is an Eular path

		"""
		V = self.graph.vertices()
		for v in V:
			size = len( self.find_children(v) )
			if size % 2 is not 0:
				return False

		return True

	def get_euler_circuit(self, s):
		"""
        The get_euler_circuit shows an Euler circuit starting from a root node

		Parameters
		----------
		s : Vertex
            The start point

		Return
		------
		circuit : Vertex list
            A list representing the Euler path
		"""

		circuit = [ s ]
		old_graph = { key:value for key,value in self.graph.get().items() }
		current = s

		while True:
			child_already_found = False
			size = self.graph.len_edges()
			if size == 0:
				break

			children = self.find_children(current)

			for child in children:
				if not self.is_bridge( (current, child) ):
					circuit.append(child)
					self.graph.remove_edge( ( current, child) )
					self.graph.remove_edge( (child, current) )
					current = child
					child_already_found = True
					break

			if not children:
				break

			if not child_already_found:
				child = children[0]
				circuit.append(child)
				self.graph.remove_edge( (current, child) )
				self.graph.remove_edge( (child, current) )
				current = child

		self.graph.set(old_graph)

		return circuit


v = [Vertex(i) for i in range(8)]

g = {
	 v[0]:[ v[1], v[2] ],
	 v[1]:[ v[0], v[3] ],
	 v[2]:[ v[0], v[3] ],
	 v[3]:[ v[4], v[6] ],
	 v[4]:[ v[3], v[5], v[6], v[7] ],
	 v[5]:[ v[4], v[6] ],
	 v[6]:[ v[3], v[4], v[5], v[7] ],
	 v[7]:[ v[4], v[6] ]
	 }

g2 = {
	v[0]: [v[1], v[2]],
	v[1]: [v[0], v[3]],
	v[2]: [v[0], v[3]],
	v[3]: [v[4], v[6]],
	v[4]: [v[3] ],
	v[5]: [v[4], v[6]],
	v[6]: [v[3], v[4], v[5], v[7]],
	v[7]: [v[4], v[6]]
	 }


G = graph(g)

B = BFS( G, v, v[0])

print( B.get_euler_circuit(v[0]) )
