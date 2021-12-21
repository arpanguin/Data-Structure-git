"""First it will check the smallest number by comparing the front element and then swap to the front one
after another
Comparisons : O(n**2)
Swapping : O(n)
"""


def selection_sort(values):
    length = len(values)

    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if values[j] < values[min_index]:
                min_index = j
                temp = values[i]
                values[i] = values[min_index]
                values[min_index] = temp
    return values


values = [3, 5, 8, 9, 6, 2]
print('Original Array:', values)
selection_sort(values)
print('Sorted Array:', values)
