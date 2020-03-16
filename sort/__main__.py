import json
from random import randint, seed
import time

import matplotlib.pyplot as plt

from sort.bubblesort import bubblesort
from sort.mergesort import mergesort
from sort.selectionsort import selectionsort
from sort.insertionsort import insertionsort
from sort.quicksort import quicksort

seed()


def create_array(array_length=10):
    array = []
    for _ in range(array_length):
        array.append(randint(0, 1000))

    return array


def log_sorting(func, array):
    func(array)
    print(array, array == sorted(array), func.__name__)


def validate_sorting_algorithms():
    random_array = create_array()
    print(random_array)

    log_sorting(mergesort, random_array[:])
    log_sorting(bubblesort, random_array[:])
    log_sorting(selectionsort, random_array[:])
    log_sorting(insertionsort, random_array[:])
    log_sorting(quicksort, random_array[:])


def generate_sorting_stats(elements=None):

    elements = list(range(1000, 10000, 1000))
    stats = {
        "elements": elements,
        "algorithms": {}
        }
    stats["elements"] = elements
    arrays = []
    # algorithms = (mergesort, bubblesort, selectionsort, insertionsort, quicksort)
    algorithms = (mergesort, quicksort)
    # algorithms = (mergesort, bubblesort)
    for n in elements:
        arrays.append(create_array(array_length=n))

    for func in algorithms:
        print(func.__name__)
        stats["algorithms"][func.__name__] = []
        for random_array in arrays:
            start = time.clock()
            func(random_array[:])
            stop = time.clock()
            stats["algorithms"][func.__name__].append((stop - start) * 1000)

    print(stats)
    # with open("fast.json", 'w') as f:
    #     f.write(json.dumps(stats))

    return stats


def generate_plot(file=None, stats=None):
    if file:
        with open(file, 'r') as f:
            stats = json.loads(f.read())

    fig = plt.figure()
    ax = plt.axes()
    plt.title("Time complexity of sorting algorithms")
    plt.xlabel("Number of elements to sort [-]")
    plt.ylabel("Time [ms]")

    for name, times in stats["algorithms"].items():
        ax.plot(stats["elements"], times, label=name)
        ax.legend()

    plt.grid()
    plt.show()


if __name__ == '__main__':
    # validate_sorting_algorithms()

    # stats = generate_sorting_stats()
    # generate_plot(stats=stats)

    generate_plot(file="stats.json")
    generate_plot(file="fast.json")
