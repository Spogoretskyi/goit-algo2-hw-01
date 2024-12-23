import random
import big_o

from typing import List, Tuple


# 1. Пошук максимального та мінімального елементів за допомогою "розділяй і володарюй"
def find_min_max(arr: List[int]) -> Tuple[int, int]:
    def divide_and_conquer(low: int, high: int) -> Tuple[int, int]:
        if low == high:
            return arr[low], arr[low]

        if high == low + 1:
            return (min(arr[low], arr[high]), max(arr[low], arr[high]))

        mid = (low + high) // 2
        left_min, left_max = divide_and_conquer(low, mid)
        right_min, right_max = divide_and_conquer(mid + 1, high)

        return min(left_min, right_min), max(left_max, right_max)

    if not arr:
        raise ValueError("Array can`t be empty")

    return divide_and_conquer(0, len(arr) - 1)


# 2. Пошук k-го найменшого елемента за допомогою Quick Select
def quick_select(arr: List[int], k: int) -> int:
    if not (1 <= k <= len(arr)):
        raise ValueError("k shoud be from 1 to array length")

    def partition(low: int, high: int) -> int:
        pivot = arr[high]
        i = low
        for j in range(low, high):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[high] = arr[high], arr[i]
        return i

    def quick_select_helper(low: int, high: int, k_smallest: int) -> int:
        if low == high:
            return arr[low]

        pivot_index = partition(low, high)

        if k_smallest == pivot_index:
            return arr[pivot_index]
        elif k_smallest < pivot_index:
            return quick_select_helper(low, pivot_index - 1, k_smallest)
        else:
            return quick_select_helper(pivot_index + 1, high, k_smallest)

    return quick_select_helper(0, len(arr) - 1, k - 1)


if __name__ == "__main__":
    # Завдання 1: Пошук мінімуму та максимуму
    array_generator = lambda n: [random.randint(1, 100) for _ in range(n)]

    best, others = big_o.big_o(find_min_max, array_generator)
    print(f"1:")
    print(best)

    # Завдання 2: Пошук k-го найменшого елемента
    array_generator2 = lambda n: [random.randint(1, 100) for _ in range(n)]
    k = random.randint(1, 10)

    def quick_select_wrapper(arr):
        return quick_select(arr, k)

    best1, others1 = big_o.big_o(quick_select_wrapper, array_generator2)
    print(f"2:")
    print(best1)
