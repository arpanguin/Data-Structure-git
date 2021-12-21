"""Similar to insertion sort
Initially Gap = length/2 and compare ith element to gap element from right and swap and then left and swap
then Gap = gap/2 and continue the same process
when gap is 0 then swapping completes
"""


def ShellSort(values):
    length = len(values)
    gap = length // 2
    while gap > 0:
        for i in range(gap, length):
            temp = values[i]
            j = i
            while j >= gap and

            if right_gap < length and values[i] > values[right_gap]:
                temp = values[i]
                values[i] = values[right_gap]
                values[right_gap] = temp
            if left_gap >= 0 and values[i] < values[left_gap]:
                temp = values[i]
                values[i] = values[left_gap]
                values[left_gap] = temp
        gap //= 2


values = [3, 5, 2, 8, 9, 11, 10, 1]
print('Original Array:', values)
ShellSort(values)
print('Sorted Array:', values)
