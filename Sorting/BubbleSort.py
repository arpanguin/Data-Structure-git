"""
It will check ith element and i+1th element and swap and keep the highest elements at last, then reduce length by 1
and continue with remaining elements.
Comparison: O(n**2)
Swapping: O(n**2)
"""


def bubbleSort(array):
    is_sorted = False
    counter = 0
    while not is_sorted:
        index = 0
        is_sorted = True
        while index < len(array)-1-counter:	# On every eteration the biggest element is sorted to last, so minusing the last element represented by counter
            if array[index] > array[index+1]:
                array[index], array[index+1] =  array[index+1], array[index]
                is_sorted = False
            index += 1
        counter += 1
    return array


values = [3, 5, 8, 9, 6, 2]
print('Original Array:', values)
bubbleSort(values)
print('Sorted Array:', values)
