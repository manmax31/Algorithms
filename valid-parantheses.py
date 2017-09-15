# Time:  O(n)
# Space: O(n)
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
#
# The brackets must close in the correct order, "()" and "()[]{}"
# are all valid but "(]" and "([)]" are not.


def is_valid(s):
    stack = []
    lookup = {"(": ")", "{": "}", "[": "]"}
    for bracket in s:
        if bracket in lookup:
            stack.append(bracket)
        else:
            if len(stack)==0 or lookup[stack.pop()] != bracket:
                return False
    return len(stack) == 0


def is_valid_with_characters(s):
    stack = []
    lookup = {"(": ")", "{": "}", "[": "]"}
    for character in s:
        if character in lookup:
            stack.append(character)
        elif character in lookup.values():
            if lookup[stack.pop()] != character:
                return False
        else:
            continue
    return len(stack) == 0

if __name__ == "__main__":
    print(is_valid_with_characters("()[]{}"))
    print(is_valid_with_characters("()[{]}"))
    print(is_valid_with_characters("(M)[A]{N}"))
    print(is_valid_with_characters("(M)[{A]}N"))
