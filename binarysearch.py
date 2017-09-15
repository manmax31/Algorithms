def binarysearch(arr, x):
    if not arr:
        return False
    else:
        mid = len(arr) // 2
        if arr[mid] == x:
            return True
        else:
            if x < arr[mid]:
                return binarysearch(arr[:mid], x)
            else:
                return binarysearch(arr[mid+1:], x)

arr = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binarysearch(arr, 13))
print(binarysearch(arr,  3))
