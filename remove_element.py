"""
Remove Element

Given an array and a value, remove all the instances of that value in the array.
Also return the number of elements left in the array after the operation.
It does not matter what is left beyond the expected length.

Example:
If array A is [4, 1, 1, 2, 1, 3]
and value elem is 1,
then new length is 3, and A is now [4, 2, 3]
Try to do it in less than linear additional space complexity.
"""


def removeElement(A, B):
    k = 0
    n = len(A)
    if n == 0:
        return A
    for i in range(n):
        if A[i] == B:
            k += 1
        elif k > 0:
            A[i-k] = A[i] # subtracting k removes all

    A = A[:n - k]
    return A, n - k


a = [4, 1, 1, 2, 1, 3]
b = 1

print(removeElement(a, b))