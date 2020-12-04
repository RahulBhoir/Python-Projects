def SelectionSort(array):
    length = len(array)
    for i in range(length-1):
        min_index = i
        for j in range(i + 1, length):
            if array[j] < array[min_index]:
                min_index = j
        array[min_index], array[i] = array[i], array[min_index]
    return array


l = [2, 4, 5, 1]
sorted_list = SelectionSort(l)
print('sorted array:', sorted_list)
