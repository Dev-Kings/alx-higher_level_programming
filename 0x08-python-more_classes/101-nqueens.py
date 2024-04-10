#!/usr/bin/python3
import sys


def queen_is_safe(chess_board, row, col, N):
    # Check if there is a queen on the same column
    for i in range(row):
        if chess_board[i][col] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if chess_board[i][j] == 1:
            return False

    # Check upper diagonal on right side
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if chess_board[i][j] == 1:
            return False

    return True


def solved(chess_board, row, N):
    if row >= N:
        return True

    for i in range(N):
        if queen_is_safe(chess_board, row, i, N):
            chess_board[row][i] = 1
            if solved(chess_board, row + 1, N):
                return True
            chess_board[row][i] = 0
    return False


def solve_n_queens(N):
    chess_board = [[0] * N for _ in range(N)]
    chess_posn = []
    if not solved(chess_board, 0, N):
        print("Solution not found")
        return False
    for i in range(N):
        for j in range(N):
            if (chess_board[i][j] == 1):
                chess_posn.append([i, j])
    print(chess_posn)
    return True


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    solve_n_queens(N)
