"""
Leetcode Problem 0413
Difficulty: Medium
Runtime: 26ms (74.85% faster)
Memory usage: 13.5mb (84.85% less)

Description:
An integer array is called arithmetic if it consists of at least 3 elements
and the difference between any two consecutive elements is the same.
Given an integer array nums, return the number of arithmetic subarrays of nums.
"""

def numberOfArithmeticSlices(nums):
    if len(nums) < 3: return 0
    reset = False
    diff = nums[1] - nums[0]
    cons = 1
    slices = 0
    for i in range(len(nums) - 1):
        if reset:
            slices += int((cons - 2) * (cons - 1) * 0.5)
            cons = 2
            reset = False
        if nums[i + 1] - nums[i] != diff:
            reset = True
            diff = nums[i + 1] - nums[i]
        else: cons += 1
    slices += int((cons - 2) * (cons - 1) * 0.5)
    return slices

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 9, 11, 14, 17, 18, 19]
    result = numberOfArithmeticSlices(nums)
    print(result)
