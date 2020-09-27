class Vertex:
    def __init__(self, val):
        self.val = val


class Edge:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight


class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, val):
        vertex = Vertex(val)
        self.adjacency_list[vertex] = []
        return vertex

    def add_edge(self, start, end, weight=1):
        if start not in self.adjacency_list:
            raise KeyError('Start Vertex is not in the Graph')
        if end not in self.adjacency_list:
            raise KeyError('End Vertex is not in the Graph')

        edge = Edge(end, weight)
        adjacencies = self.adjacency_list[start]
        adjacencies.append(edge)

    def get_nodes(self):
        return set(self.adjacency_list.keys())

    def get_neighbors(self, vertex):
        if not vertex in self.adjacency_list:
            raise KeyError('Given Vertex is not in the Graph')

        edges = self.adjacency_list[vertex]

        return [{'vertex': edge.vertex,
                 'weight': edge.weight} for edge in edges]

    def size(self):
        return len(self.get_nodes())
