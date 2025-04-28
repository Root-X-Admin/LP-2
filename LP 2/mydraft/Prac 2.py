import heapq

class PuzzleState:
    def __init__(self, board, moves=0, previous=None):
        self.board = board
        self.moves = moves
        self.previous = previous
        self.zero_pos = self.find_zero()
        self.priority = self.moves + self.heuristic()

    def find_zero(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return (i, j)

    def heuristic(self):
        """ Manhattan distance heuristic """
        distance = 0
        goal = {
            1: (0, 0), 2: (0, 1), 3: (0, 2),
            4: (1, 0), 5: (1, 1), 6: (1, 2),
            7: (2, 0), 8: (2, 1)
        }
        for i in range(3):
            for j in range(3):
                value = self.board[i][j]
                if value != 0:
                    (goal_x, goal_y) = goal[value]
                    distance += abs(i - goal_x) + abs(j - goal_y)
        return distance

    def get_neighbors(self):
        neighbors = []
        x, y = self.zero_pos
        directions = [(-1,0), (1,0), (0,-1), (0,1)]  # Up, Down, Left, Right

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < 3 and 0 <= ny < 3:
                new_board = [row[:] for row in self.board]
                new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]
                neighbor = PuzzleState(new_board, self.moves + 1, self)
                neighbors.append(neighbor)

        return neighbors

    def __lt__(self, other):
        return self.priority < other.priority

def reconstruct_path(state):
    path = []
    while state:
        path.append(state)
        state = state.previous
    return path[::-1]

def astar(start_board):
    start_state = PuzzleState(start_board)
    open_list = []
    heapq.heappush(open_list, start_state)
    visited = set()

    while open_list:
        current = heapq.heappop(open_list)

        if current.heuristic() == 0:
            return reconstruct_path(current)

        visited.add(tuple(map(tuple, current.board)))

        for neighbor in current.get_neighbors():
            if tuple(map(tuple, neighbor.board)) not in visited:
                heapq.heappush(open_list, neighbor)

    return None

def print_board(board):
    for row in board:
        print(' '.join(str(num) for num in row))
    print()

# ------------------------------
# Initial State
start_board = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

# Solve the puzzle
path = astar(start_board)

# Display steps
if path:
    print("Steps to reach the goal:")
    print("---------")
    for state in path:
        print_board(state.board)
        print("---------")
else:
    print("No solution found.")
