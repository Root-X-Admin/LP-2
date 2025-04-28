import heapq

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        (current_distance, current_vertex) = heapq.heappop(pq)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

graph = {}
n = int(input("Enter number of edges: "))
for _ in range(n):
    u, v, w = input("Enter edge (u v w): ").split()
    w = int(w)
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append((v, w))
    graph[v].append((u, w))
start = input("Enter starting vertex: ")
distances = dijkstra(graph, start)
print("Shortest distances from", start + ":", distances)
