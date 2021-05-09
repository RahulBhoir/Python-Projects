def FindMinMax(arr):
    max_val, min_val = 0, 1000
    for i in range(len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
        elif arr[i] < min_val:
            min_val = arr[i]
    return min_val, max_val
    # pythonic way
    # return min(arr), max(arr)


arr = [21, 3, 4]

min_val, max_val = FindMinMax(arr)
print(min_val, max_val)
