from collections import Counter

def isAnagram(s, t):
    return Counter(s) == Counter(t)

s = 'Anagram'
t = 'nagaram'
print(isAnagram(s.lower(), t.lower()))