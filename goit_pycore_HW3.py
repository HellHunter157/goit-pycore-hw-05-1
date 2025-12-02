import random
import timeit



small = list(range(100))
random.shuffle(small)

medium = list(range(500))
random.shuffle(medium)

large = list(range(1000))
random.shuffle(large)



def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


time_insertion_medium = timeit.timeit(
    lambda: insertion_sort(medium.copy()), number=5
)

time_insertion_large = timeit.timeit(
    lambda: insertion_sort(large.copy()), number=5
)

time_timsort_medium = timeit.timeit(
    lambda: sorted(medium), number=5
)

time_timsort_large = timeit.timeit(
    lambda: sorted(large), number=5
)

time_merge_medium = timeit.timeit(
    lambda: merge_sort(medium.copy()), number=5
)

time_merge_large = timeit.timeit(
    lambda: merge_sort(large.copy()), number=5
)


# --- Вивід ---
print("Insertion sort (medium):", time_insertion_medium)
print("Insertion sort (large): ", time_insertion_large)

print("Python Timsort (medium):", time_timsort_medium)
print("Python Timsort (large): ", time_timsort_large)

print("Merge sort (medium):", time_merge_medium)
print("Merge sort (large): ", time_merge_large)
