# Given an array of integers, every element appears twice except for one. Find that single one.
# Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
# Input : [1 2 2 3 1]
# Output : 3

from collections import Counter


def singleNumber(A):
    counts = Counter(A)
    for i in A:
        if counts[i] == 1:
            return i
    return None


def singleNumber1(A):
    """Bitwise XOR
    XOR will return 1 only on two different bits. So if two numbers are the same, XOR will return 0.
    :param A: 
    :return: 
    """
    ret = A[0]
    for i in range(1, len(A)):
        ret ^= A[i]
    return ret


print(singleNumber([1, 2, 2, 3, 1]))
print(singleNumber1([1, 2, 2, 3, 1]))

