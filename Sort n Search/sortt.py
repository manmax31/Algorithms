from heapq import merge, heapify, heappop


def quicksort(arr):
    if not arr:
        return False
    pivot   = [x for x in arr if x == arr[0]]
    lesser  = [x for x in arr if x  < arr[0]]
    greater = [x for x in arr if x  > arr[0]]

    return quicksort(lesser) + pivot + quicksort(greater)


def heapsort(arr):
    arr = arr.copy()
    heapify(arr)
    return [heappop(arr) for i in range(len(arr))]


def mergesort(arr):
    if not arr:
        return False

    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]

    left = mergesort(left)
    right = mergesort(right)
    return list(merge(left, right))



arr = [3, 2, 1, 0, 5, 10]

print("Quick Sort:", quicksort(arr))
print("Heap Sort:", heapsort(arr))
print("Merge Sort:", mergesort(arr))
