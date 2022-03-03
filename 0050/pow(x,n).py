"""
Leetcode Problem 0050
Difficulty: Medium
Runtime: 12ms (97.75% faster)
Memory usage: 13.4MB (68.99% less)

Description:
Return x raised to the power of n.
"""

def myPow(x, n):
    if n == 0: return 1
    elif n > 0: return power(x, n)
    else: return 1 / power(x, n * (-1))

def power(x, n):
    if n == 1: return x
    if n == 2: return x * x
    temp = power(x, n // 2)
    if n % 2 == 0: return temp * temp
    else: return temp * temp * x

if __name__ == "__main__":
    x = 2
    n = -5
    result = myPow(x, n)
    print(result)
