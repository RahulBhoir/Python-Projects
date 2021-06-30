def bestSum(target, numbers, memo):
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None
    shortest_combination = None
    for num in numbers:
        remainder = target - num
        ans = bestSum(remainder, numbers, memo)
        if ans != None:
            combination = [num, *ans]
            if shortest_combination is None or len(shortest_combination) > len(combination):
                shortest_combination = combination
    memo[target] = shortest_combination
    return shortest_combination


print(bestSum(100, [1, 2, 25], dict()))
