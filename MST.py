from collections import defaultdict

class Graph:

	def __init__(self, vertices):
		self.Vertices = vertices
		self.graph = []

	def add_edge(self, a, b, w):
		self.graph.append([a, b, w])

	def MST(self):

		result = []

		n = self.Vertices
		m = len(self.graph)

		# sort edges in ascending order by weight
		self.graph = sorted(self.graph,
							key=lambda data: data[2])

		tree_id = []
		for i in range(n):
			tree_id.append(i)

		cost = 0
		for i in range(m):

			a, b, w = self.graph[i]

			if (tree_id[a] != tree_id[b]):
				cost += w
				result.append ( [a, b, w] )

				old_id = tree_id[b]  
				new_id = tree_id[a]

				for j in range(n):
					if (tree_id[j] == old_id):
						tree_id[j] = new_id
		
		return [result, cost]
