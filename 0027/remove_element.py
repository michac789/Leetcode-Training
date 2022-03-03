"""
Leetcode Problem 0027
Difficulty: Easy
Runtime: 14ms (97.44% faster)
Memory usage: 13.4MB (66.27% less)

Description:
Given an integer array nums and an integer val,
remove all occurences of val in nums in-place.
"""

def removeElement(nums, val):
    i = 0
    length = len(nums)
    while i < length:
        if val == nums[i]:
            nums.pop(i) 
            length -= 1
        else: i += 1
    return len(nums)

if __name__ == "__main__":
    nums = [3, 2, 2, 3, 3, 4]
    val = 2
    result = removeElement(nums, val)
    print(result)
    print(nums)
