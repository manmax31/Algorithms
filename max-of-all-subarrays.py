"""
Given an array and an integer k, find the maximum for each and every contiguous subarray of size k.
arr = [1, 2, 3, 1, 4, 5, 2, 3, 6], k=3
output = [3, 3, 4, 5, 5, 5, 6]
http://www.geeksforgeeks.org/maximum-of-all-subarrays-of-size-k/
http://stackoverflow.com/questions/39885520/finding-the-max-of-each-continguous-subarray-of-a-given-size
"""


def first_soln(arr, k):
    """
    Outer loop runs for O(n-k+1), inner loop for k times.
    TimeComplexity: O(n-k+1)*k = O(nk)
    :param arr:
    :param k:
    :return:
    """
    output = []
    for i in range(k-1, len(arr)):
        max_ = max(arr[i-(k-1):i+1])
        output.append(max_)
    return output


def second_soln(arr, win):
    from collections import deque
    # Q contains indexes of items in the window that are greater than
    # all items to the right of them.  This always includes the last item
    # in the window.
    # An element is useful if it is in current window and is greater than all other elements on
    # left side of it in current window.
    Q, win_maxes = deque(), list()

    """
    https://www.youtube.com/watch?v=39grPZtywyQ
    O(n)
    Extra Space: O(k)
    Q contains indices of elements
    for i in range(k):
        1. Remove all indices j from rear end of Q if arr[j] < arr[i]
        2. Add index i to Q
    First index in Q corresponds to largest element of current sub array of size k
    """
    for i in range(win):
        print(i)
        while len(Q) > 0 and  arr[Q[-1]] <= arr[i]:
            Q.pop()
        Q.append(i)
    print('Q:', list(Q))
    win_maxes.append(arr[Q[0]])
    print('Win_Max', win_maxes)

    """
    for i in range(k, len(arr)):
        1. Append element corresponding to first index of Q
        2. Remove all indices from front of Q which won't be included in current window of size k.
        3. Remove all indices j from rear end of Q if arr[j] < arr[i]
        4. Add index i to Q
    Append element corresponding to first index of Q
    """
    for i in range(win, len(arr)):
        # remove indexes (at most 1, really) left of window
        print('\ni:', i)
        print('Q:', list(Q))
        while len(Q) > 0 and Q[0] <= (i - win):
            Q.popleft()
            print('After Pop Left Q:', list(Q))

        # remove anything that isn't greater than the new item
        while len(Q) > 0 and arr[i] >= arr[Q[-1]]:
            Q.pop()
            print('After Pop Right Q:', list(Q))
        Q.append(i)
        print('Q:', list(Q))
        win_maxes.append(arr[Q[0]])
        print('Win_Max', win_maxes)



arr = [2, 5, 3, 4, 1]
win = 3

# print(first_soln(arr, win))
second_soln(arr, win)



