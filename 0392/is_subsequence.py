"""
Leetcode Problem 0392
Runtime: 20ms (85.10% faster)
Memory usage: 13.5mb (88.10% less)

Description:
Given two strings s and t, returns true if s is a subsequence of t,
otherwise false.
"""

def isSubsequence(s, t):
    i = 0
    if len(s) == 0: return True
    for letter in t:
        if letter == s[i]: i += 1
        if i == len(s): return True
    return False

if __name__ == "__main__":
    s = "hgd"
    t = "ahbgdc"
    result = isSubsequence(s, t)
    print(result)
