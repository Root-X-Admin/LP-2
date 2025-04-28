# 4.	Implement a solution for a Constraint Satisfaction Problem using Backtracking for n-queens problem.

def solve_n_queens(n):
    def backtrack(row):
        if row == n:
            # All queens are placed successfully
            board = []
            for i in range(n):
                row_str = '.' * queens[i] + 'Q' + '.' * (n - queens[i] - 1)
                board.append(row_str)
            solutions.append(board)
            return

        for col in range(n):
            if col in columns or (row - col) in diagonals1 or (row + col) in diagonals2:
                continue  # Not safe, skip

            # Place queen
            queens[row] = col
            columns.add(col)
            diagonals1.add(row - col)
            diagonals2.add(row + col)

            backtrack(row + 1)

            # Backtrack (remove the queen)
            queens[row] = -1
            columns.remove(col)
            diagonals1.remove(row - col)
            diagonals2.remove(row + col)

    solutions = []
    queens = [-1] * n  # queens[i] = column of queen in row i
    columns = set()
    diagonals1 = set()  # row - col
    diagonals2 = set()  # row + col

    backtrack(0)
    return solutions

# Example: Solve 4-Queens
n = int(input("Enter the value of n for n-queens problem: "))
result = solve_n_queens(n)
for solution in result:
    for row in solution:
        print(row)
    print()
