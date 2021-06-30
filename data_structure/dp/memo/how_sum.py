def howSum(target, numbers, ans, memo):
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None
    for num in numbers:
        remainder = target - num
        ans = howSum(remainder, numbers, ans, memo)
        if ans != None:
            ans.append(num)
            memo[target] = ans
            return memo[target]
    memo[target] = None
    return None


# print(howSum(2, [1, 2], []))
# print(howSum(7, [5, 3, 4, 7], []))
# print(howSum(7, [2, 4], []))
# print(howSum(8, [2, 3, 5], []))
# print(howSum(0, [1, 2], []))
print(howSum(400, [3, 4, 2], [], dict()))
print(howSum(300, [7, 14], [], dict()))
