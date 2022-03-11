"""
It will check ith element and i+1th element, if ith element is bigger then start new loop from i+1 to 0 and check if
j < j-1 then swap
Comparison complexity : O(n**2)
Swapping complexity : O(n)
Note : forward then backward
"""


def insertionSort(array):
    i = 0
    while i < len(array) - 1:
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
            j = i
            while j > 0:
                if array[j] < array[j - 1]:
                    array[j], array[j - 1] = array[j - 1], array[j]
                else:  # it is only checking with the previous element if bigger then break.
                    break
                j -= 1
        i += 1
    return array


values = [3, 1, 2]
print('Original Array:', values)
insertionSort(values)
print('Sorted Array:', values)
