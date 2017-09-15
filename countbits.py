"""
Write an efficient program to count number of 1s in binary representation of an integer.

Examples

Input : n = 6
Output : 2
Binary representation of 6 is 110 and has 2 set bits

Input : n = 13
Output : 3
Binary representation of 11 is 1101 and has 3 set bits
"""

def count_bits(n):
    """
    >> 1 divides a number by 2
    Loop through all bits in an integer, check if a bit is set and if it is then increment the set bit count
    Theta(log n)
    :param n:
    :return:
    """
    count = 0
    while n:
        count += n & 1
        n = n >> 1
    return count


def count_bits_brian(n):
    """
    Subtraction of 1 from a number toggles all the bits (from right to left) till the rightmost set bit
    So if we subtract a number by 1 and do bitwise & with itself (n & (n-1)), we unset the righmost set bit.
    If we do n & (n-1) in a loop and count the no of times loop executes we get the set bit count.
    Loop executes as many 1s in n
    O(log n)
    :param n:
    :return:
    """
    count = 0
    while n:
        n &= n-1
        count += 1
    return count


num = 5
print(count_bits(num))
print(count_bits_brian(num))