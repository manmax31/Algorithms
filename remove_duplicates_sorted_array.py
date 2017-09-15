"""
Remove duplicates from Sorted Array
Given a sorted array, remove the duplicates in place such that each element appears only once and return the new length.

Note that even though we want you to return the new length, make sure to change the original array as well in place

Do not allocate extra space for another array, you must do this in place with constant memory.

Example:
Given input array A = [1,1,2],
Your function should return length = 2, and A is now [1,2].
"""


def remove_duplicates(A):
    k = 0
    n = len(A)
    if n == 0:
        return A
    for i in range(n-1):
        if A[i] == A[i+1]:
            k += 1
        elif k > 0:
            A[i-(k-1)] = A[i+1] # subtracting k removes only 1

    A = A[:n-k]
    return n-k, A


a = [1, 1, 2, 3, 3, 4, 4, 4]
print(remove_duplicates(a))