"""
It will check ith element and i+1th element and swap and keep the highest elements at last, then reduce length by 1
and continue with remaining elements.
Comparison: O(n**2)
Swapping: O(n**2)
"""


def BubbleSort(values):
    length = len(values)
    while length > 0:
        for i in range(length - 1):
            if values[i] > values[i + 1]:
                temp = values[i]
                values[i] = values[i + 1]
                values[i + 1] = temp
        length -= 1


values = [3, 5, 8, 9, 6, 2]
print('Original Array:', values)
BubbleSort(values)
print('Sorted Array:', values)
