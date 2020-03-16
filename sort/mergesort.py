def mergesort(array):
    if len(array) > 1:
        middle = len(array)//2
        left = array[:middle]
        right = array[middle:]

        mergesort(left)
        mergesort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1


if __name__ == '__main__':
    from random import seed
    from random import randint

    seed(1)
    array = []
    for _ in range(10):
        array.append(randint(0, 100))

    print(array)
    mergesort(array)
    print(array)
    print(array == sorted(array))
