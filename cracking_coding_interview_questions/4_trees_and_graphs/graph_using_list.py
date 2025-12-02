# dict/list/tuples representation of graph e.g.
# {"A": [(B,5), (D,7)]
#  "B": [(A,5), (C,9), (E,2)]
#  "C": [(B,9), (E,4)]
#  "D": [(A,7)]
#  "E": [(B,2), (C,4)]
# }


class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbours = list()

    def add_neighbour(self, v, weight):
        if v not in self.neighbours:
            self.neighbours.append((v, weight))
        #self.neighbours.sort()


class Graph:

    def __init__(self):
        self.vertices = dict()

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex

    def add_edge(self, vertex1, vertex2, weight):
        if vertex1.name in self.vertices.keys() and vertex2.name in self.vertices.keys():
            self.vertices[vertex1.name].add_neighbour(vertex2, weight)
            self.vertices[vertex2.name].add_neighbour(vertex1, weight)
            return True
        else:
            return False

    def print_graph(self):
        for key,value in self.vertices.items():
            all_neighbours = ""
            for neighbour in value.neighbours:
                all_neighbours += str(neighbour[0].name + ",") + str(neighbour[1])
                all_neighbours += "; "
            all_neighbours.strip('; ')
            print(key + " --> {0}".format(all_neighbours))


g = Graph()
a = Vertex("A")
b = Vertex("B")
c = Vertex("C")
d = Vertex("D")
e = Vertex("E")
g.add_vertex(a)
g.add_vertex(b)
g.add_vertex(c)
g.add_vertex(d)
g.add_vertex(e)
g.add_edge(a, b, 5)
g.add_edge(a, d, 7)
g.add_edge(b, c, 9)
g.add_edge(b, e, 2)
g.add_edge(c, e, 4)
g.print_graph()