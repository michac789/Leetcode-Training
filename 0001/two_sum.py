"""
Leetcode Problem 0001
Difficulty: Easy
Runtime: 69ms (70.38% faster)
Memory usage: 14.3MB (70.95% less)

Description:
Given an array of integers nums and an integer target, return the indices
of the two numbers such that they add up to target.
"""
  
def twoSum(nums, target):
    dict = {}
    for iter, value in enumerate(nums):
        key = target - value
        if key in dict: return[dict[key], iter]
        dict[value] = iter

if __name__ == "__main__":
    nums = [2, 11, 7, 15]
    target = 9
    result = twoSum(nums, target)
    print(result)
