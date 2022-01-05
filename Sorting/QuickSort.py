"""
QuickSort uses divide and conquer method. It chooses a pivot element and check all the element left to pivot must be
smaller and all the right element must be greater. Pivot element can be chosen first, last or randomly.
Time Complexity : O(n**2)
Space : O(log(n))
"""


def quickSort(array):
    quickSort_helper(array, 0, len(array) - 1)
    return array


def quickSort_helper(array, start_idx, end_idx):
    if start_idx >= end_idx:
        return

    pivot_idx = start_idx
    left_idx = start_idx + 1
    right_idx = end_idx

    while left_idx <= right_idx:
        if array[left_idx] > array[pivot_idx] > array[right_idx]:
            # if left index greater and right index smaller that pivot then swap left and right index
            swap(array, left_idx, right_idx)
        elif array[left_idx] <= array[pivot_idx]:
            left_idx += 1
        elif array[right_idx] >= array[pivot_idx]:
            right_idx -= 1

    swap(array, pivot_idx, right_idx)
    # divide and conquer method start
    is_left_subarray_smaller = right_idx - 1 - start_idx < end_idx - (right_idx + 1)
    if is_left_subarray_smaller:
        quickSort_helper(array, start_idx, right_idx - 1)
        quickSort_helper(array, right_idx + 1, end_idx)
    else:
        quickSort_helper(array, right_idx + 1, end_idx)
        quickSort_helper(array, start_idx, right_idx - 1)


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


print(quickSort([8, 5, 2, 9, 5, 6, 3]))
