# TO-DO: complete the helper function below to merge 2 sorted arrays
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


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here

    return arr


# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    pass


def merge_sort_in_place(arr, l, r):
    pass

