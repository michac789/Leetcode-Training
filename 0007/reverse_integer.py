"""
Leetcode Problem 0007
Difficulty: Medium
Runtime: 23ms (75.41% faster)
Memory usage: 13.3MB (65.29% less)

Description:
Given a signmed 32-bit integer x, return x with its digit reversed.
If reversing caused the value to go outside the signed 32-bit range, return 0.
"""

def reverse(x):
    if x == 0: return 0
    s = str(x)
    if x >= 0:
        s = s[::-1]
    else:
        s = s[:0:-1]
    cut = 0
    for letter in s:
        if letter == "0":
            cut += 1
        else: break
    s = s[cut::]
    if x < 0: s = "-" + s
    s = int(s)
    if s < -2**31 or s > 2**31 - 1: return 0
    return s

if __name__ == "__main__":
    input = -10500
    result = reverse(input)
    print(result)
