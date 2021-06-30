import numpy as np


def gridTraveler(row, col):
    if row == 0 or col == 0:
        return 0
    if row == 1 and col == 1:
        return 1
    return gridTraveler(row - 1, col) + gridTraveler(row, col - 1)


# print(gridTraveler(0, 3))  # 0
# print(gridTraveler(1, 1))  # 1
# print(gridTraveler(2, 3))  # 3
# print(gridTraveler(3, 3))  # 6
# print(gridTraveler(18, 18))  # 2333606220


def gridTravelerDp(row, col, memo):
    print(np.array(memo))
    if memo[row][col] != -1:
        return memo[row][col]
    if row == 0 or col == 0:
        return 0
    if row == 1 and col == 1:
        return 1
    memo[row][col] = gridTravelerDp(
        row - 1, col, memo) + gridTravelerDp(row, col - 1, memo)
    return memo[row][col]


m, n = 2, 3
memo = [[-1 for i in range(n+1)] for j in range(m+1)]
print(gridTravelerDp(m, n, memo))  # 2333606220
