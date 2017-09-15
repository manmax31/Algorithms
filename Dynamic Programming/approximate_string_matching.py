"""
Given 2 strings, how many EDIT, DELETE, EDIT operations are needed to convert one string to another
We can compute the edit distance between two strings by working from the ends.
The three operations available to us are:
1. ADD: Add one character to the end of a string
2. DELETE: Remove one character from the end of a string
3. EDIT: Change the character at the end of a string.
https://secweb.cs.odu.edu/~zeil/cs361/web/website/Lectures/styles/pages/editdistance.html
https://www.youtube.com/watch?v=We3YDTzNXEk
Eg: ABCDEF -> AZCED
1. EDIT D to F
2. DELETE D
3. EDIT B to Z

In the matrix:
If x and y are different then we fill up a cell, we look at min(left of cell, diagonally up of cell, top of cell) + 1
If x == y, then we fill up a cell = diagonally up of cell
 Time complexity is O(m*n)
 Space complexity is O(m*n)
"""
import pprint as pp


def edit_distance(target, source):
    t, s = len(target), len(source)
    distance = [[None for i in range(s+1)] for j in range(t+1)]

    for i in range(s+1):
        distance[0][i] = i
    for i in range(t+1):
        distance[i][0] = i

    for i in range(1, t+1):
        for j in range(1, s+1):
            if target[i-1] == source[j-1]:
                distance[i][j] = distance[i-1][j-1]
            else:
                distance[i][j] = 1 + min(distance[i-1][j], distance[i-1][j-1], distance[i][j-1])
    pp.pprint(distance)
    return distance[t][s]

source = 'abcdef'
target = 'azced'
print('Minimum Edit Distance:', edit_distance(target, source))





