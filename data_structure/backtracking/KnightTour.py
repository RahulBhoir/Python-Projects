import numpy as np


def KnightTour(n):
    board = [[-1 for i in range(n)] for j in range(n)]
    KnightTourHelper(n=n, board=board, row=0, col=0, counter=0)
    print(np.array(board))


def KnightTourHelper(n, board, row, col, counter):
    if counter == n*n:
        return True

    if row < 0 or col < 0 or row >= n or col >= n or board[row][col] != -1:
        return False

    # do
    board[row][col] = counter

    # recur
    row_possible = [-2, -2, -1, -1, 1, 1, 2, 2]
    col_possible = [-1, 1, -2, 2, -2, 2, -1, 1]
    for r_move, c_move in zip(row_possible, col_possible):
        if KnightTourHelper(n, board, row + r_move, col + c_move, counter + 1):
            return True

    # undo
    board[row][col] = -1
    return False


KnightTour(7)
