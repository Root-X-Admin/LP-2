import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # Cost from start to node
        self.h = 0  # Heuristic cost to goal
        self.f = 0  # Total cost

    def __lt__(self, other):
        return self.f < other.f

def heuristic(a, b):
    # Manhattan distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, end):
    start_node = Node(start)
    end_node = Node(end)
    open_list = []
    closed_set = set()
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_set.add(current_node.position)

        if current_node.position == end_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        (x, y) = current_node.position
        neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

        for next_pos in neighbors:
            if (0 <= next_pos[0] < len(grid)) and (0 <= next_pos[1] < len(grid[0])) and grid[next_pos[0]][next_pos[1]] == 0:
                if next_pos in closed_set:
                    continue
                neighbor = Node(next_pos, current_node)
                neighbor.g = current_node.g + 1
                neighbor.h = heuristic(neighbor.position, end_node.position)
                neighbor.f = neighbor.g + neighbor.h
                heapq.heappush(open_list, neighbor)

    return None

# Example grid (0 = walkable, 1 = wall)
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
grid = []
for i in range(rows):
    row = list(map(int, input(f"Enter row {i+1} (0 for walkable, 1 for wall): ").split()))
    grid.append(row)
start = tuple(map(int, input("Enter start position (row col): ").split()))
end = tuple(map(int, input("Enter end position (row col): ").split()))
path = astar(grid, start, end)
print("Path found:", path)
