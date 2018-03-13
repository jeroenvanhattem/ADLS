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
		"""
        The get functions returns the graph

		Return
		------
		self.G : graph

		"""
		return self.G

	def sort_nodes(self, row):
		"""
        The sort_nodes function sorts a row of vertices

		Parameters
		----------
		row : Vertex list
            The list to be sorted

		Return
		------
		row : Vertex list
            The sorted list
            
		"""
		size = len(row)

		for i in range(size):
			for j in range(size-1-i):
				if row[j] > row[j+1]:
					row[j], row[j + 1] = row[j + 1], row[j]

		return row

	def add_node(self, list, value):
		"""
        The add_node function adds a node and sorts it right away.

		Parameters
		----------
		list : vertex list
            The list of existing vertices
		value : vertex
            The to be added vertex

		Return
		------
		new_edge : Vertex list
            The updated Vertex list, including the recently added node

		"""
		list.append(value)
		new_edge = self.sort_nodes(list)
		return new_edge

	def remove_edge(self, e):
		"""
        The add_edge function removes an edge between two nodes.

		Parameters
		----------
		e : edge
            The edge existing out of two vertices.

		"""
		graph = self.G

		u = e[0]
		value = e[1]

		edge = graph.get(u)
		if value in edge: edge.remove(value)

	def add_edge(self, e):
		"""
        The add_edge function adds an edge between two nodes.

		Parameters
		----------
		e : edge
            The edge existing out of two vertices.

		"""
		graph = self.G

		u = e[0]
		value = e[1]

		edge = graph.get(u)
		new_edge = self.add_node(edge, value)
		graph.update({u: new_edge})

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

	def get_bridges(self):
		"""
        The get_bridges finds and returns bridges

        Return
        ------
        bridges: list
        Sorted list of bridges

        """
		bridges = []
		E = self.graph.edges()

		for u, v in E:
			self.graph.remove_edge( (u, v) )
			self.graph.remove_edge( (v, u) )
			path = self.show_path( v, u )

			if v not in path:
				bridges.append( (u,v) )
				bridges.append( (v,u) )

			self.graph.add_edge( (u, v) )
			self.graph.add_edge( (v, u) )

		return sorted( list( set(bridges) ) )



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


G = graph(g)

B = BFS( G, v[1] )

print( B.get_bridges() )

