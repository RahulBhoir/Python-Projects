def gridTraveler(row, col):
    grid = [[0 for i in range(col + 1)] for j in range(row + 1)]
    grid[1][1] = 1
    for i in range(row + 1):
        for j in range(col + 1):
            current = grid[i][j]
            if j+1 <= col:
                grid[i][j+1] += current
            if i+1 <= row:
                grid[i+1][j] += current
    print(grid[row][col])


gridTraveler(18, 18)
gridTraveler(2, 3)
gridTraveler(3, 3)
