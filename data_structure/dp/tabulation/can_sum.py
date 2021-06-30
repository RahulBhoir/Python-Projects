def canSum(target, numbers):
    table = [False for i in range(target+1)]
    table[0] = True
    for i in range(target+1):
        if table[i] == True:
            for num in numbers:
                if i + num <= target:
                    table[i + num] = True
    return table[target]


# tc = O(mn)
print(canSum(7, [5, 3, 4, 7]))  # True
print(canSum(7, [2, 3]))  # True
print(canSum(7, [2, 4]))  # False
print(canSum(8, [2, 3, 5]))  # True
print(canSum(300, [7, 14]))  # False
