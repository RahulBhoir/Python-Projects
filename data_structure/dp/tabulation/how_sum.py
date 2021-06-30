def howSum(target, numbers):
    table = [None for i in range(target+1)]
    table[0] = []
    for i in range(target + 1):
        if table[i] != None:
            for num in numbers:
                if i + num <= target:
                    table[i + num] = list(table[i])
                    table[i + num].append(num)
    return table[target]


# tc = O(m^2 * n)
# sc = O(m^2)
print(howSum(7, [5, 3, 4]))  # True
print(howSum(7, [2, 3]))  # True
print(howSum(7, [2, 4]))  # False
print(howSum(8, [2, 3, 5]))  # True
print(howSum(300, [7, 14]))  # False
