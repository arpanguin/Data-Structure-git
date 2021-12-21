def binary_search(value_list, search_key, left_index, right_index):
    if left_index > right_index:
        return -1
    else:
        middle_index = (left_index + right_index) // 2
        if search_key == value_list[middle_index]:
            return middle_index
        elif search_key > value_list[middle_index]:
            return binary_search(value_list=value_list, search_key=search_key, left_index=middle_index + 1,
                                 right_index=right_index)
        else:
            return binary_search(value_list=value_list, search_key=search_key, left_index=left_index,
                                 right_index=middle_index - 1)


values = input("Enter the values comma separated : ")
list_of_values = values.split(',')
search_key = input("Enter the key to search : ")

position = binary_search(value_list=list_of_values, search_key=search_key, left_index=0,
                         right_index=len(list_of_values) - 1)

if position != -1:
    print(f"{search_key} found in : {position + 1} position")
else:
    print(f"Unable to found {search_key}")
