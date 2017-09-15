# Time:  O(n)
# Space: O(n)

# Given an array of integers, return indices of the two numbers
# such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution.
#
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


def twoSum(arr, target):
    """
    If the target = x+y or y = target-x,
    If target = 1, and if we know x is 2,  then y has to be -1 or (y = 1-2)
                       if we know x is -3, then y has to be 4  or (y = 1-(-3)), ...
    In a dict, for every x we have seen, we store what y we are looking for i.e y = index of x.
    As we loop through, if we find that y in the array, we are done and we return index of x and index of y
    """
    look_for = {}
    for i, x in enumerate( arr ):
        try:
            print('Find:', look_for[x], i)
            return look_for[x], i
        except KeyError:
            look_for.setdefault(target - x, i)



print(twoSum([2, 7, -1, 15, 1], 3))
