def InsertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


l = [23, 2, 4, 5, 1]
sorted_list = InsertionSort(l)
print('sorted array:', sorted_list)
