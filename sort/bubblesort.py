# Optimized, short version.
def bubblesort(array):
    is_sorted = False
    passes_needed = len(array) - 1
    while not is_sorted and passes_needed > 0:
        is_sorted = True
        for i in range(passes_needed):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                is_sorted = False
        passes_needed -= 1
