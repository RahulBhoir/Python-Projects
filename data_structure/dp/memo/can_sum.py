def canSum(target, numbers):
    if target == 0:
        return True
    if target < 0:
        return False
    for num in numbers:
        remainder = target - num
        if canSum(remainder, numbers) == True:
            return True

    return False


# print(canSum(7, [2, 3]))  # True
# print(canSum(7, [5, 3, 4, 7]))  # True
# print(canSum(7, [2, 4]))  # False
# print(canSum(8, [2, 3, 5]))  # True
# print(canSum(300, [7, 14]))  # False


# using dp
print('using dp')


def canSumDp(target, numbers, memo):
    if target in memo:
        return memo[target]
    if target == 0:
        return True
    if target < 0:
        return False
    for num in numbers:
        remainder = target - num
        if canSumDp(remainder, numbers, memo) == True:
            memo[target] = True
            return True
    memo[target] = False
    return False


print(canSumDp(7, [5, 3, 4, 7], dict()))  # True
print(canSumDp(7, [2, 3], dict()))  # True
print(canSumDp(7, [2, 4], dict()))  # False
print(canSumDp(8, [2, 3, 5], dict()))  # True
print(canSumDp(300, [7, 14], dict()))  # False
