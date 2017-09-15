"""
Given a column title as appears in an Excel sheet, return its corresponding column number.
Example:
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28

Solution:
Imagine AAB: A*26^2 + A*26^1 + B*26^0
In this case A=1, B=2, ..., Z=26
"""

import string


def titleToNumber(A):
    # alist = list(map(lambda x: x - 64, map(ord, A)))
    # total = 0
    # for i, val in enumerate(alist[::-1]):
    #     total += val * 26 ** i
    # return total
    # OR
    characters = string.ascii_uppercase
    pos = 0
    for i, character in enumerate(A[::-1]):
        val = characters.index(character) + 1
        pos += val * (26 ** i)
    return pos

print(titleToNumber('AB'))
print(titleToNumber('AAA'))

