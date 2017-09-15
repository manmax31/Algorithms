"""
Reverse digits of an integer.
Example1:
x = 123,
return 321

Example2:
x = -123,
return -321

Return 0 if the result overflows and does not fit in a 32 bit signed integer
"""


def reverse(A):
    A = str(A)
    if A[0] == '-':
        A = '-' + A[1:][::-1]
    else:
        A = A[::-1]
    A = int(A)
    if A > 2 ** 31 or A < -2 ** 31:
        return 0
    return A

print(reverse(321))

