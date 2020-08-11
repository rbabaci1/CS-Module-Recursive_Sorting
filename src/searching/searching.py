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
    isAsc, start, end = False, 0, len(arr) - 1
    if len(arr) >= 2:
        if arr[0] < arr[-1]:
            isAsc = True

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


# def isAscending(arr):
#     if len(arr) >= 2:
#         if arr[0] < arr[1]:
#             return True
#         return False

# def agnostic_recursive_binary_search(arr, target, start=0, end=None):
#     isAsc = isAscending(arr)
#     if not end:
#         end = len(arr) - 1
#     midpoint = (start + end) // 2
#     # base cases
#     if start > end:
#         return -1
#     if arr[midpoint] == target:
#         return midpoint

#     if isAsc:
#         if arr[midpoint] > target:
#             return agnostic_binary_search(arr, target, start, midpoint - 1)
#         else:
#             return agnostic_binary_search(arr, target, midpoint + 1, end)
#     else:
#         if arr[midpoint] > target:
#             return agnostic_binary_search(arr, target, midpoint + 1, end)
#         else:
#             return agnostic_binary_search(arr, target, start, midpoint - 1)
#     return -1
