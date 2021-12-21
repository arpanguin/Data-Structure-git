"""
It will check ith element and i+1th element, if ith element is bigger then start new loop from i+1 to 0 and check if
j < j-1 then swap
Comparison complexity : O(n**2)
Swapping complexity : O(n)
"""


def insertion_sort(values):
    length = len(values)
    for i in range(1, length):
        position = i
        while position > 0 and values[position-1] > values[position]:
            temp = values[position]
            values[position] = values[position-1]
            values[position-1] = temp
            position -= 1
    return values


values = [3, 5, 2, 8, 9, 11, 10, 1]
print('Original Array:', values)
insertion_sort(values)
print('Sorted Array:', values)
