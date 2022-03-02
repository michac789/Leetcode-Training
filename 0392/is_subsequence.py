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
