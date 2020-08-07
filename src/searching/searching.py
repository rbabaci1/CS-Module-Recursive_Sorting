# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    midpoint = (start + end) // 2
    if start > end:
        return -1
    if arr[midpoint] == target:
        return midpoint

    if arr[midpoint] > target:
        return binary_search(arr, target, start, midpoint - 1)
    else:
        return binary_search(arr, target, midpoint + 1, end)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
def agnostic_binary_search(arr, target):
    start, end, isAsc = 0, len(arr) - 1, False
    for i in range(len(arr)):
        if arr[i] < arr[i + 1]:
            isAsc = True
        break

    while start <= end:
        midpoint = (start + end) // 2
        if arr[midpoint] == target:
            return midpoint
        if isAsc:
            if arr[midpoint] > target:
                end = midpoint - 1
            else:
                start = midpoint + 1
        else:
            if arr[midpoint] > target:
                start = midpoint + 1
            else:
                end = midpoint - 1
    return -1
