def BubbleSort(arr):
    length = len(arr)
    for _ in range(length):
        for j in range(length - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


l = [23, 2, 4, 5, 1]
sorted_list = BubbleSort(l)
print('sorted array:', sorted_list)
