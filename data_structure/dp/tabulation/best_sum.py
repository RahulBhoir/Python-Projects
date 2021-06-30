def bestSum(target, numbers):
    table = [None for i in range(target + 1)]
    table[0] = []
    for i in range(target + 1):
        if table[i] != None:
            for num in numbers:
                if i + num <= target:
                    temp = list(table[i])
                    temp.append(num)
                    if table[i + num] == None or len(temp) < len(table[i + num]):
                        table[i + num] = temp
    return table[target]


print(bestSum(7, [5, 3, 4]))  # True
print(bestSum(7, [2, 3, 1]))  # True
print(bestSum(7, [2, 4]))  # False
print(bestSum(8, [2, 3, 5]))  # True
print(bestSum(300, [7, 14]))  # False
