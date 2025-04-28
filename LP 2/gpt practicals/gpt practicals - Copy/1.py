from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # Undirected

    def dfs_util(self, v, visited):
        visited.add(v)
        print(v, end=' ')
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.dfs_util(neighbor, visited)

    def dfs(self, start):
        visited = set()
        print("DFS Traversal:")
        self.dfs_util(start, visited)
        print()

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        print("BFS Traversal:")
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                print(vertex, end=' ')
                visited.add(vertex)
                for neighbor in self.graph[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        print()

# Example usage
g = Graph()
n = int(input("Enter number of edges: "))
for _ in range(n):
    u, v = map(int, input("Enter edge (u v): ").split())
    g.add_edge(u, v)
start = int(input("Enter starting vertex for DFS and BFS: "))
g.dfs(start)
g.bfs(start)
