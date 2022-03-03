"""
Leetcode Problem 0014
Difficulty: Easy
Runtime: 25ms (70.79% faster)
Memory usage: 13.7MB (64.33% less)

Description:
Find the longest common prefix string amongst an array of strings
"""

def longestCommonPrefix(strs):
    output = strs[0]
    for i in range(len(strs) - 1):
        min_len = min(len(strs[i]), len(strs[i + 1]))
        for j in range(min_len):
            if strs[i][j] != strs[i + 1][j]:
                min_len = j
                break
        output = output[:min_len]
    return output

if __name__ == "__main__":
    strs = ["flower", "flow", "flights"]
    result = longestCommonPrefix(strs)
    print(result)
