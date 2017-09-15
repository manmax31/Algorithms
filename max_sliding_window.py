"""
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to
the very right.
You can only see the k numbers in the window. Each time the sliding window moves right by one position.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

 Therefore, return the max sliding window as [3,3,5,5,6,7].

Time Complexity: O(n)

https://discuss.leetcode.com/topic/19055/java-o-n-solution-using-deque-with-explanation

At each i, we keep "promising" elements, which are potentially max number in window [i-(k-1),i] or any subsequent window. This means

If an element in the deque and it is out of i-(k-1), we discard them. We just need to poll from the head, as we are using a deque and elements are ordered as the sequence in the array

Now only those elements within [i-(k-1),i] are in the deque. We then discard elements smaller than a[i] from the tail. This is because if a[x] <a[i] and x<i, then a[x] has no chance to be the "max" in [i-(k-1),i], or any other subsequent window: a[i] would always be a better candidate.

As a result elements in the deque are ordered in both sequence in array and their value. At each step the head of the deque is the max element in [i-(k-1),i]
"""

from collections import deque


def max_sliding_window(nums, k):
    output = []
    dq = deque()  # Q to store Index. Head of Q always store MAX value in that window
    for i, num in enumerate(nums):
        if dq and dq[0] < i-k+1:  # Remove all Out of window max values
            dq.popleft()
        while dq and nums[dq[-1]] < num:  # Remove all smaller predecessors
            dq.pop()
        dq.append(i)
        if i > k-2:
            output.append(nums[dq[0]])
    return output


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(max_sliding_window(nums, k))
