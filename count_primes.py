import math

def count_primes(n):
    """
    Get prime numbers with upper bound n
    Time Complexity: O(n log log n)
    :param n:
    :return:
    """
    composite, prime = [], []
    count = 0
    for i in range(2, n+1):
        if i not in composite:
            prime.append(i)
            count += 1
            for j in range(i**2, n+1, i):
                composite.append(j)
    print(count)
    return prime

print(count_primes(10))