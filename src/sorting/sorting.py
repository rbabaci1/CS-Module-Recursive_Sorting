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
    if len(arr) > 1:
        midpoint = len(arr) // 2
        left = merge_sort(arr[:midpoint])
        right = merge_sort(arr[midpoint:])

        arr = merge(left, right)
    return arr


# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    start2 = mid + 1
    # if last value in first arr is less then first value in second arr
    # simply return, values already sorted
    if arr[mid] <= arr[start2]:
        return

    while start <= mid and start2 <= end:
        if arr[start] <= arr[start2]:
            start += 1
        else:
            value, index = arr[start2], start2
            while start != index:
                arr[index] = arr[index - 1]
                index -= 1
            arr[start] = value

            start += 1
            mid += 1
            start2 += 1


def merge_sort_in_place(arr, l, r):
    if l < r:
        mid = (l + r) // 2

        merge_sort_in_place(arr, l, mid)
        merge_sort_in_place(arr, mid + 1, r)
        merge_in_place(arr, l, mid, r)

    return arr
