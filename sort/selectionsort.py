def selectionsort(array):
    for i in range(len(array)):
        index_min = i
        for j in range(i + 1, len(array)):
            if array[j] < array[index_min]:
                index_min = j
        array[i], array[index_min] = array[index_min], array[i]
