"""
Given an array A of integers and another non negative integer k, find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.

Example :

Input :

A : [1 5 3]
k : 2
Output :

1
as 3 - 1 = 2

Return 0 / 1 for this problem.

Solution:
We are looking to find pair of integers where A[i] - A[j] = k, k being known entity
Lets say we fix A[i] ( i.e. we know A[i]), do we know what A[j] should be ?
A[j] = A[i] - k.

We can store all the numbers in a hashmap / hashset and then lookup A[j] in it to find out if A[j] exists.

Corner case : How do you handle case when k = 0 cleanly ?
"""

from collections import Counter

def diffij(A, k):
    A = sorted(A)
    n = len(A)
    if n == 0:
        return 0
    i = 0
    j = 1
    while i < n and j < n:
        if i != j and A[j] - A[i] == k:
            return 1
        elif A[j] - A[i] < k:
            j += 1
        else:
            i += 1
    return 0


def diffij_hash(A, k):
    n = len(A)
    hash_dict = Counter(A)

    for i in range(n):
        ai = A[i]
        aj = ai - k

        if aj in hash_dict:
            if k == 0:
                if hash_dict[aj] >= 2:
                    return 1
            else:
                return 1

    return 0


a = (1, 5, -3, 4, 10, 4)
k = 0
print(diffij_hash(a, k))

fmap = {
        "pets_allowed": ["dogs", "dog", "cats", "cat"],
        "no_or_low_fee": ["no fee", "nofee", "no  fee", "nofee", "no_fee", "lowfee", "reduced_fee", "low_fee", "reduced fee", "low fee"],
        "furnished": ["furnished"],
        "outdoor_space": ["outdoor space", "garden", "terrace", "balcony", "roof deck"],
        "prewar": ("prewar", "pre_war", "pre war"),
        "facilities": ("dishwasher", "fireplace", "laundry", "swimming", "health", "gym", "fitness", "training", "internet", "elevator"),
        "parking": ("parking", "garage"),
        "transport": ("train", "subway", "transport"),
        "utilities": ("utilities", "heat water", "water included"),
        "new_construction": ("new_construction", "new"),
        "dining_room": ("dining")
    }