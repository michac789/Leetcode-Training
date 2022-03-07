"""
Leetcode Problem 0003
Difficulty: Medium
Runtime: 61ms (69.69% faster)
Memory usage: 13.5MB (86.91% less)

Description:
Given a string s, return the length of the longest substring
without repeating characters.
"""

def lengthOfLongestSubstring(s):
    used = []
    length = 0
    result = 0
    for letter in s:
        if letter in used:
            if length > result: result = length
            index = used.index(letter)
            length = length - index - 1
            used = used[index + 1::]
        used.append(letter)
        length += 1
    if length > result: result = length
    return result

if __name__ == "__main__":
    string = "dvdf"
    result = lengthOfLongestSubstring(string)
    print(result)
