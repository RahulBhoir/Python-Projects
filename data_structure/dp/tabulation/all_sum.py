def allSum(target, numbers):
    table = [[None, ] for i in range(target + 1)]
    table[0][0] = []
    for i in range(target + 1):
        if table[i][0] != None:
            for num in numbers:
                if i + num <= target:
                    temp = list(table[i])
                    temp[i].append(num)
                    table[i + num][0] = list(temp)
    print(table)


allSum(2, [1, 2, 3])
