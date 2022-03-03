"""
Leetcode Problem 0009
Difficulty: Easy
Runtime: 50ms (94% faster)
Memory usage: 13.3MB (87.89% less)

Description:
Given an integer x, return true if x is palindrome otherwise false
"""

def isPalindrome(x):
    if x < 0: return False
    number = str(x)
    for i in range(len(number) // 2):
        if number[i] != number[-(i + 1)]: return False
    return True

if __name__ == "__main__":
    x = 12344321
    result = isPalindrome(x)
    print(result)
