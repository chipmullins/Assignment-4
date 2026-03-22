from typing import List


def heapify(arr: List[int], n: int, i: int) -> None:
    """
    Ensures the subtree rooted at index i satisfies the max-heap property.
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def build_max_heap(arr: List[int]) -> None:
    """
    Converts an unsorted array into a max-heap.
    """
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)


def heapsort(arr: List[int]) -> List[int]:
    """
    Sorts an array in ascending order using Heapsort.
    """
    n = len(arr)
    build_max_heap(arr)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr


if __name__ == "__main__":
    sample = [12, 11, 13, 5, 6, 7]
    print("Original array:", sample)
    print("Sorted array:", heapsort(sample.copy()))