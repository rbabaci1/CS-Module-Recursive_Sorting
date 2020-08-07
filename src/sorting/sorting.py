# merges two arrays and sorts the result
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr, j, k = [0] * elements, 0, 0

    for i in range(len(merged_arr)):
        if j != len(arrA) and k != len(arrB):
            if arrA[j] < arrB[k]:
                merged_arr[i] = arrA[j]
                j += 1
            else:
                merged_arr[i] = arrB[k]
                k += 1
        elif j < len(arrA):
            merged_arr[i] = arrA[j]
            j += 1
        else:
            merged_arr[i] = arrB[k]
            k += 1
    return merged_arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    midpoint = len(arr) // 2
    left = arr[:midpoint]
    right = arr[midpoint:]

    merge_sort(left)
    merge_sort(right)
    merged_arr = merge(left, right)
    for i in range(len(merged_arr)):
        arr[i] = merged_arr[i]

    return arr


# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    pass


def merge_sort_in_place(arr, l, r):
    pass

