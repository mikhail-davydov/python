def quicksort(arr):
    if len(arr) < 2:
        return arr
    pivot_index = len(arr) // 2
    pivot = arr[pivot_index]
    left = []
    right = []
    for i in range(0, len(arr)):
        if i == pivot_index:
            continue
        left.append(arr[i]) if arr[i] < pivot else right.append(arr[i])
    return quicksort(left) + [pivot] + quicksort(right)

print(quicksort([1, 20, 3, 4, 112, 6, 7, 8, 9, 10]))