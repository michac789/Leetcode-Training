"""
Leetcode Problem 0035
Difficulty: Easy
Runtime: 36ms (82.86% faster)
Memory usage: 14MB (95.92% less)

Description:
TODO
"""

def searchInsert(nums, target): 
    middle = len(nums) // 2
    left = nums[:middle]
    mid = nums[middle]
    right = nums[(middle + 1):]
    if target == mid: return middle
    elif target > mid:
        if right: return middle + 1 + searchInsert(right, target)
        else: return middle + 1
    elif target < mid:
        if left: return searchInsert(left, target)
        else: return middle

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    target = 4.7
    result = searchInsert(nums, target)
    print(result)
