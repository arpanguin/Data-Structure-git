"""First it will check the smallest number by comparing the front element and then swap to the front one
after another
Comparisons : O(n**2)
Swapping : O(n)
"""


def selection_sort(array):
    for i in range(len(array)):
        smallest = i
        for j in range(i + 1, len(array)):
            if array[smallest] > array[j]:
                smallest = j
        array[i], array[smallest] = array[smallest], array[i]
    return array


values = [3, 5, 8, 9, 6, 2]
print('Original Array:', values)
selection_sort(values)
print('Sorted Array:', values)
