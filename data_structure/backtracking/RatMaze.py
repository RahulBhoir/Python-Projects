import numpy as np


def RatMaze():
    maze = [[1, 0, 0, 0, 0],
            [1, 1, 0, 1, 0],
            [0, 1, 0, 0, 0],
            [1, 1, 1, 1, 0],
            [0, 0, 0, 1, 1]]
    solArr = [[0 for i in range(len(maze))] for j in range(len(maze))]
    MazeHelper(maze=maze, row=0, col=0, solArr=solArr)
    print(np.array(solArr))


def MazeHelper(maze, row, col, solArr):
    # base condition
    if row == len(maze) - 1 and col == len(maze) - 1:
        solArr[row][col] = 1
        return True

    if isSafe(maze, row, col, len(maze)):
        # do
        solArr[row][col] = 1
        # recur
        if MazeHelper(maze, row+1, col, solArr):
            return True
        if MazeHelper(maze, row, col + 1, solArr):
            return True
        # undo
        solArr[row][col] = 0
        return False
    return False


def isSafe(maze, row, col, n):
    if (row < n) and (col < n) and (maze[row][col] == 1):
        return True
    return False


RatMaze()
