"""
Leetcode Problem 0020
Difficulty: Easy
Runtime: 19ms (85.63% faster)
Memory usage: 13.5MB (83.35% less)

Description:
Given string s containing (, [, {, determine if the parentheses is valid.
"""

def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    # () [] {}
    stack = []
    for letter in s:
        if letter == '(': stack.append(')')
        elif letter == '[': stack.append(']')
        elif letter == '{': stack.append('}')
        elif letter in [')', ']', '}']:
            if len(stack) == 0: return False
            if letter != stack.pop(): return False
    if len(stack) != 0: return False
    return True

if __name__ == "__main__":
    input = "{([(sfksd)][sf])..}"
    result = isValid(input)
    print(result)
