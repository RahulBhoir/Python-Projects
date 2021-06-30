def NQueens(board, row, col, total_queens, currently_placed_queens, ans):

    if total_queens == currently_placed_queens:
        print(ans)
        return

    if col == len(board):
        row += 1
        col = 0

    if row == len(board):
        return

    # place the Queen
    if isItSafeToPlaceQueen(board, row, col):
        # do
        board[row][col] = 1

        # recur
        # NQueens(board, row, col + 1, total_queens, currently_placed_queens + 1, ans +
        #         '[' + str(row) + ', ' + str(col) + ']')
        NQueens(board, row, col + 1, total_queens,
                currently_placed_queens + 1, board)

        # undo
        board[row][col] = 0

    # not place
    NQueens(board, row, col+1, total_queens, currently_placed_queens, ans)


def isItSafeToPlaceQueen(board, row, col):
    # horizontally left
    i = col - 1
    while i >= 0:
        if board[row][i] == 1:
            return False
        i -= 1

    # vertically left
    j = row - 1
    while j >= 0:
        if board[j][col] == 1:
            return False
        j -= 1

    # left diagonal
    i = row - 1
    j = col - 1
    while j >= 0 and i >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # right diagonal
    r = row - 1
    c = col + 1
    while r >= 0 and c < len(board[0]):
        if board[r][c] == 1:
            return False
        r -= 1
        c += 1

    return True


# n = int(input('Enter the numbers of Queens: '))
n = 4
board = [[0 for i in range(n)] for i in range(n)]

# (matrix, rol, col, total_queens, currently_placed_queens, ans)
NQueens(board, 0, 0, n, 0, board)
