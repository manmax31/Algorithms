"""
Given an array of size n, find the majority element. The majority element is the element that appears more than floor(n/2) times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example :

Input : [2, 1, 2]
Return  : 2 which occurs 2 times which is greater than 3/2. 

https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm
Time: O(n)
Space: O(1)
"""

from collections import Counter


def majority_element(A):
    i = 0
    for element in A:
        if i == 0:
            m, i = element, 1
        elif m == element:
            i += 1
        else:
            i -= 1
    return m



s = [2, 1, 2, 1, 1]
print(majority_element(s))