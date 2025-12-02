# Source: https://www.youtube.com/watch?v=-uR7BSfNJko
class Vertex:
	def __init__(self, name):
		self.name = name
		self.color = "black"
		self.distance = float("Inf")
		self.neighbours = list()

	def add_neighbour(self, v):
		if v not in self.neighbours:
			self.neighbours.append(v)
			self.neighbours.sort()

class Graph:
	def __init__(self):
		self.vertices = dict()

	def add_vertex(self, v):
		if isinstance(v, Vertex) and v.name not in self.vertices.keys():
			self.vertices[v.name] = v
			return True
		else:
			return False

	def add_edge(self, u, v):
		if u in self.vertices and v in self.vertices:
			for key,value in self.vertices.items():
				if key == u:
					value.add_neighbour(v)
				if key == v:
					value.add_neighbour(u)
			return True
		else:
			return False

	def print_graph(self):
		for key, value in self.vertices.items():
			print(key + " --> " + str(self.vertices[key].neighbours) + " " + str(self.vertices[key].distance))

	def bfs(self, vert):
		vert.distance = 0
		vert.color = "red"
		queue = list()
		for neighbour in vert.neighbours:
			queue.append(neighbour)
			self.vertices[neighbour].distance = vert.distance + 1
		while len(queue) > 0:
			u = queue.pop()
			node_u = self.vertices[u]
			node_u.color = "red"
			for v in node_u.neighbours:
				node_v = self.vertices[v]
				if node_v.color == "black":
					queue.append(v)
					if node_v.distance > node_u.distance + 1:
						node_v.distance = node_u.distance + 1

g = Graph()
a = Vertex('A')
g.add_vertex(a)
g.add_vertex(Vertex('B'))
for i in range(ord('A'), ord('K')):
	g.add_vertex(Vertex(chr(i)))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
	g.add_edge(edge[0], edge[1])
g.bfs(a)
g.print_graph()