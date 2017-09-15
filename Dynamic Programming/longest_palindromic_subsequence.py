# Given a string S, find the longest palindromic substring in S.
# You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
# String s is palindrome if:
# 1. First and Last chars should match
# 2. Substring (excluding first and last chars) is palindrome
# https://www.youtube.com/watch?v=obBdxeCx_Qs


import numpy as np


def longest_palindromic_substring(s):
    n = len(s)
    palindrome_begins_at = 0  # index where longest palindrome begins
    max_len = 1               # length of longest palindrome

    # Initialisation palindrome and Trivial Case: Single Letter Palindromes
    palindrome = [[True if x == y else None for y in range(n)] for x in range(n)]

    # Finding palindromes of 2 characters
    for i in range(n-1):
        if s[i] == s[i+1]:
            palindrome[i][i+1] = True
            palindrome_begins_at = i
            max_len = 2

    # Finding palindromes of length 3 to n and saving the longest
    for cur_len in range(3, n):
        for i in range(n-cur_len+1):
            j = i + cur_len - 1
            # 1. The first and last characters should match
            # #2. Rest of the substring should be a palindrome
            if s[i] == s[j] and palindrome[i+1][j-1]:
                palindrome[i][j] = True
                palindrome_begins_at = i
                max_len = cur_len

    return s[palindrome_begins_at:max_len + palindrome_begins_at]

print(longest_palindromic_substring("bananas"))



