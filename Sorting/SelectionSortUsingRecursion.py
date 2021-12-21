# First it will check the smallest number by comparing and then swap to the front one after another

def selection_sort(values, start_index=0, compare_with_index=0, compare_to_index=1):
    length = len(values)

    if start_index < length:
        if compare_to_index < length:
            current_smallest_index = compare_to_index if values[compare_with_index] > values[compare_to_index] \
                else compare_with_index
            selection_sort(values, start_index=start_index, compare_with_index=current_smallest_index,
                           compare_to_index=compare_to_index + 1)
        else:
            temp = values[compare_with_index]
            values[compare_with_index] = values[start_index]
            values[start_index] = temp
            start_index += 1
            selection_sort(values, start_index=start_index, compare_with_index=start_index,
                           compare_to_index=start_index + 1)
    return values


values = [3, 5, 8, 9, 6, 2]
print('Original Array:', values)
selection_sort(values)
print('Sorted Array:', values)
