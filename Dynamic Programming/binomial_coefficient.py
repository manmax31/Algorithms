# (n k): Number of ways to choose k things out of n possibilities
# (n k): n! / ((n-k)!k!)
import pprint as pp


def binomial_coefficient(n, k):
    bc = [[1 if j == 0 or i == j else 0 for j in range(n+1)] for i in range(n+1)]
    for i in range(n+1):
        for j in range(i):
            bc[i][j] = bc[i-1][j-1] + bc[i-1][j]
    print("Pascal's Triangle")
    pp.pprint(bc)
    return bc[n][k]

print(binomial_coefficient(5, 4))
