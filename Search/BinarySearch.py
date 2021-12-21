"""Search a sorted array by repeatedly dividing the search interval in half. Begin with an interval
covering the whole array. If the value of the search key is less than the item in the middle of the
interval, narrow the interval to the lower half. Otherwise, narrow it to the upper half. Repeatedly
check until the value is found or the interval is empty.
Time complexity : O(Log n) == Logarithm
"""


def binary_search(value_list, length, search_key):
    left_index = 0
    right_index = length - 1

    while left_index <= right_index:
        middle_index = (left_index + right_index) // 2
        if search_key == value_list[middle_index]:
            return middle_index
        elif search_key > value_list[middle_index]:
            left_index = middle_index + 1
        else:  # search_key < value_list[middle_index]
            right_index = middle_index - 1
    return -1


values = input("Enter the values comma separated : ")
list_of_values = values.split(',')
key = input("Enter the key to search : ")

position = binary_search(value_list=list_of_values, length=len(list_of_values), search_key=key)

if position != -1:
    print(f"{key} found in : {position + 1} position")
else:
    print(f"Unable to found {key}")
