def print_solution(board):
    for row in board:
        print(" ".join(row))
    print()

def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 'Q':
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    return True

def solve(board, col, n):
    if col >= n:
        print_solution(board)
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 'Q'
            solve(board, col+1, n)
            board[i][col] = '.'

def n_queens(n):
    board = [['.' for _ in range(n)] for _ in range(n)]
    solve(board, 0, n)

n = int(input("Enter board size (n): "))
n_queens(n)
