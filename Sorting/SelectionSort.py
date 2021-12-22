"""First it will find the smallest number for array then swap it into front and increased the i value to 1
Comparisons : O(n**2)
Swapping : O(n)
"""


def selection_sort(array):
    for i in range(len(array)):
        smallest = i
        for j in range(i + 1, len(array)):
            if array[smallest] > array[j]:
                smallest = j
        array[i], array[smallest] = array[smallest], array[i]  # Swapping the smallest number to i'th(front) position
    return array


values = [3, 5, 8, 9, 6, 2]
print('Original Array:', values)
selection_sort(values)
print('Sorted Array:', values)
