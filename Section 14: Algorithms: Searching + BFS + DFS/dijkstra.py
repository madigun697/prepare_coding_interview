import numpy as np

graph = [[0, 0, 6, 3, 0],
[3, 0, 0, 0, 0],
[0, 0, 0, 2, 0],
[0, 1, 1, 0, 0],
[0, 4, 0, 2, 0]]

def dijkstra(graph, start):
	dist = [np.inf] * len(graph)
	dist[start] = 0
	current = start
	done = False

	while not done:
		dist, current, done = calcDist(dist, current)

	print(dist)

def calcDist(dist, current):
	visit = 0
	nextNodes = [np.inf] * len(graph)
	for i, n in enumerate(graph[current]):
		if n > 0:
			if dist[i] > dist[current] + n:
				dist[i] = dist[current] + n
				visit += 1
			nextNodes[i] = dist[i]
	
	current = np.argmin(nextNodes)
	return dist, current, visit == 0

dijkstra(graph, 4)