def partition(array, low, high):
    pivot = array[low]
    i = low + 1
    border = low + 1
    while i < high:
        if array[i] < pivot:
            array[border], array[i] = array[i], array[border]
            border += 1
        i += 1

    array[low], array[border - 1] = array[border - 1], array[low]
    return border - 1


def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array)

    if low < high:
        border = partition(array, low, high)
        quicksort(array, low, border)
        quicksort(array, border + 1, high)
