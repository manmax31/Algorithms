# Sorted Matrix Search:
# Given an M x N matrix in which each row and each column is sorted in ascending order,
# write a method to find an element.
"""
Solution
We can bring these observations together into a solution. The observations are the following : If the start of a column is greater than x, then x is to the left of the column.
If the end of a column is less than x, then x is to the right of the column.
If the start of a row is greater than x, then x is above that row.
If the end of a row is less than x, then x is below that row.
"""


def find_element(matrix, element):
    row, col = 0, len(matrix[0]) - 1
    while row < len(matrix) and col >= 0:
        if matrix[row][col] == element:
            return True
        elif matrix[row][col] > element:
            col -= 1
        else:
            row += 1
    return False
