import distances
import cities
import MST

distances = distances.get_distances()
cities = cities.get_cities()

vertices = len(distances)

graph = MST.Graph(vertices)

for city, endpoints in distances.items():
    for city2 in endpoints:
        graph.add_edge(city2['start_id'], city2['end_id'], city2['distance'])

result, cost = graph.MST()

print ("Edges of MST")
for u, v, weight in result:
	print("%s <-> %s = ~%d km" % (cities[u]['name'], cities[v]['name'], weight))

print("Total Cost => " , cost)