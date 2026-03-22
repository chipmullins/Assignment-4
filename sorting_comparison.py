import random
import time
from statistics import mean
from heapsort import heapsort


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quicksort(left) + [pivot] + quicksort(right)


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def generate_random_array(n):
    return [random.randint(0, 100000) for _ in range(n)]


def generate_sorted_array(n):
    return list(range(n))


def generate_reverse_sorted_array(n):
    return list(range(n, 0, -1))


def time_algorithm(sort_func, arr):
    arr_copy = arr.copy()
    start = time.perf_counter()
    sort_func(arr_copy)
    end = time.perf_counter()
    return end - start


def run_trials(sort_func, generator, n, trials=5):
    times = []
    for _ in range(trials):
        arr = generator(n)
        times.append(time_algorithm(sort_func, arr))
    return mean(times)


def main():
    sizes = [100, 500, 1000, 2000]
    distributions = {
        "Random": generate_random_array,
        "Sorted": generate_sorted_array,
        "Reverse Sorted": generate_reverse_sorted_array
    }

    algorithms = {
        "Heapsort": lambda arr: heapsort(arr),
        "Quicksort": quicksort,
        "Merge Sort": merge_sort
    }

    print(f"{'Size':<8}{'Distribution':<18}{'Algorithm':<15}{'Time (s)':<12}")
    print("-" * 55)

    for n in sizes:
        for dist_name, generator in distributions.items():
            for alg_name, alg_func in algorithms.items():
                avg_time = run_trials(alg_func, generator, n)
                print(f"{n:<8}{dist_name:<18}{alg_name:<15}{avg_time:<12.6f}")


if __name__ == "__main__":
    main()