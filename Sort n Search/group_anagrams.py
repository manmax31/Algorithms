# Write a method to sort an array of strings so that all the anagrams are next to
# each other.
# Time Complexity: O(n log n)
from collections import defaultdict


def group_anagrams(a):
    map_anagrams = defaultdict(list)
    for s in a:
        anagram = ''.join(sorted(s))
        map_anagrams[anagram].append(s)
    result = list()
    for v in map_anagrams.values():
        result += v
    return result


if __name__ == "__main__":
    a = ['aaa', 'bbb', 'ccc', 'abc', 'bca', 'cba']
    print(group_anagrams(a))


