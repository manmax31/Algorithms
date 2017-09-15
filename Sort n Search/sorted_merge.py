# You are given two sorted arrays, A and B,
# where A has a large enough buffer at the end to hold B.
# Write a method to merge B into A in sorted order.
# Time Complexity: O(a), Space Complexity: O(1)


def merge(a, b):
    last_a, last_b = 4, 4

    index_a, index_b, = last_a - 1, last_b - 1
    index_merged = last_a + last_a - 1

    while index_b >= 0:
        print(a[index_a], b[index_b])
        if index_a >= 0 and a[index_a] > b[index_b]:
            a[index_merged] = a[index_a]
            index_a -= 1
        else:
            a[index_merged] = b[index_b]
            index_b -= 1
        print(a[index_merged])
        index_merged -= 1

    return a


if __name__ == "__main__":
    a_list = [2, 4, 6, 7, None, None, None, None]
    b_list = [1, 3, 5, 8]
    print(merge(a_list, b_list))


