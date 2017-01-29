class Vertex:
	def __init__(self, n):
		self.name = n
		self.neighbors = list()
		
		self.distance = 9999
		self.color = 'black'
	
	def add_neighbor(self, v):
		if v not in self.neighbors:
			self.neighbors.append(v)
			self.neighbors.sort()
            #neighbors[] is a list of directly connected vertices, sorted alphabetically

class Graph:
	vertices = {}
	
	def add_vertex(self, vertex):
		if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
			self.vertices[vertex.name] = vertex
			return True
		else:
			return False
	
	def add_edge(self, u, v): #takes two connected vertices as input
		if u in self.vertices and v in self.vertices:
			for key, value in self.vertices.items():
				if key == u:
					value.add_neighbor(v)
				if key == v:
					value.add_neighbor(u)
                #adds neighboring vertices to list of vertex neighbors
			return True
		else:
			return False
			
	def print_graph(self):
		for key in sorted(list(self.vertices.keys())):
			print(key + str(self.vertices[key].neighbors) + "  " + str(self.vertices[key].distance))
            #prints list of all vertices + neighbors of that vertex, + distance to source for that vertex
		
	def bfs(self, vert):
		q = list()
		vert.distance = 0
		vert.color = 'red'
		for v in vert.neighbors:
			self.vertices[v].distance = vert.distance + 1
			q.append(v)
            #iterates through the neighbors of each vertex. 
            #adds 1 to the distance for the neighboring vertex.
            #adds neighboring vertex to the queue for iteration.
		
		while len(q) > 0:
			u = q.pop(0)
            #pops first item in queue list
			node_u = self.vertices[u]
            #sets the vertex object (not just the vertex name) to node_u
			node_u.color = 'red'
            #sets the node to state: visited
			
			for v in node_u.neighbors:
				node_v = self.vertices[v]
                #sets the vertex object of each of node_u's neighbors to node_v
				if node_v.color == 'black': #if neighbor is not yet visited:
					q.append(v) #add neighbor to the queue
					if node_v.distance > node_u.distance + 1: 
						node_v.distance = node_u.distance + 1
					#if the neighboring node's distance is greater than the distance of u + 1,
                    #that means a shorter path exists. Set neighboring node's distance equal to
                    #node_u's distance + 1.
g = Graph()
a = Vertex('A')
g.add_vertex(a)
#one method for adding each vertex to the graph. inconvenient, must be added one by one
g.add_vertex(Vertex('B'))
#another method, adds the vertex to the graph all in one line, but still must be done one by one
for i in range(ord('A'), ord('K')):
	g.add_vertex(Vertex(chr(i)))
#ideal method. iterates through range of vertex names and adds all vertices to the graph

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
#list of all the existing connections in the graph
for edge in edges:
	g.add_edge(edge[:1], edge[1:])
    #takes in 2 vertices (split by indexing from edges list) and adds each to the other's list of neighbors
	
g.bfs(a)
#runs breadth first search, starting at Vertex('A'), searching through 
#all vertices and determining their distance and neighbors.
g.print_graph()
#prints each vertex, its neighbors, and the distance from A. This is output you see.