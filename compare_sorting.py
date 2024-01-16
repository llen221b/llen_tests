import timeit
import random

def compare_sorting_algorithms(algorithm1, algorithm2, sizes, sorting_percentages):
    for size in sizes:
        for percentage in sorting_percentages:
            data = generate_data(size, percentage)

            time_algorithm1 = timeit.timeit(lambda: algorithm1(data), number=1)
            time_algorithm2 = timeit.timeit(lambda: algorithm2(data), number=1)

            print(f"Size: {size}, Sorting Percentage: {percentage}%")
            print(f"Algorithm 1 Time: {time_algorithm1} seconds")
            print(f"Algorithm 2 Time: {time_algorithm2} seconds")
            print("-----------------------")

def generate_data(size, sorting_percentage):
    data = list(range(1, size + 1))

    if sorting_percentage > 0:
        num_elements_to_shuffle = int((sorting_percentage / 100) * size)
        random.shuffle(data[:num_elements_to_shuffle])

    return data

# Przykładowe algorytmy sortowania
def quick_sort(data):
    return sorted(data)

def merge_sort(data):
    return sorted(data)

# Przykładowe wartości
sizes = [100, 500, 1000, 5000]
sorting_percentages = [0, 25, 50, 100]

compare_sorting_algorithms(quick_sort, merge_sort, sizes, sorting_percentages)

