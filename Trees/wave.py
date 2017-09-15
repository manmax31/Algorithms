"""
Given an array of integers, sort the array into a wave like array and return it,
In other words, arrange the elements into a sequence such that:
 a1 >= a2 <= a3 >= a4 <= a5.....

Example

Given [1, 2, 3, 4]

One possible answer : [2, 1, 4, 3]
Another possible answer : [4, 1, 3, 2]
NOTE : If there are multiple answers possible, return the one thats lexicographically smallest.
So, in example case, you will return [2, 1, 4, 3]

Solution:
array = {5, 1, 3, 4, 2}
Sort the above array.
array = {1, 2, 3, 4, 5}
Now swap adjacent elements in pairs.

swap(1, 2)
swap(3, 4)

Now, our array = {2, 1, 4, 3, 5}

and voila!, the array is in the wave form.
"""


def wave(A):
    A.sort()
    n = len(A)
    for i in range(0, n, 2):
        if i + 1 < n:
            A[i], A[i + 1] = A[i + 1], A[i]
    return A



l = [1, 2, 3, 4]
print(wave(l))



