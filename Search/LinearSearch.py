"""Its sequential search where each element will be checked until the key is found
    Time complexity : O(n) == Linear"""


def linear_search(value_list, length, search_key):
    index = 0
    while index < length:
        if value_list[index] == search_key:
            return index
        index += 1
    return -1


values = input("Enter the values comma separated : ")
list_of_values = values.split(',')
key = input("Enter the key to search : ")

position = linear_search(value_list=list_of_values, length=len(list_of_values), search_key=key)

if position != -1:
    print(f"{key} found in : {position + 1} position")
else:
    print(f"Unable to found {key}")
