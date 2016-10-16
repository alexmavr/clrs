# Insertion sort (in-place)
# Worst-case time O(n^2)
# Best-case time Theta(n)
# Space Theta(1)
def insertion_sort(array):
    if len(array) < 2:
        return array
    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        while j >= 0 and array[j] > key:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    return array

assert insertion_sort([4]) == [4]
assert insertion_sort([4, 1]) == [1, 4]
assert insertion_sort([1, 2]) == [1, 2]
assert insertion_sort([4, 1, 3, 5]) == [1, 3, 4, 5]
assert insertion_sort([1, 3, 5, 7, 9]) == [1, 3, 5, 7, 9]
assert insertion_sort([9, 7, 5, 3, 1]) == [1, 3, 5, 7, 9]
assert insertion_sort([1, 9, 3, 7, 5]) == [1, 3, 5, 7, 9]
