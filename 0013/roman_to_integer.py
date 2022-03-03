"""
Leetcode Problem 0013
Runtime: ___ms (__% faster)
Memory usage: ___mb (__% less)

Description:
Given a valid roman numeral, convert it into integer.
I: 1, V: 5, X: 10, L: 50, C: 100, D: 500, M: 1000
IV: 4, IX: 9, XL: 40, XC: 90, CD: 400, CM: 900
"""

def romanToInt(s):
    result = 0
    cont = False
    for i in range(len(s)):
        if cont:
            cont = False
            continue
        if s[i] == "M": result += 1000
        elif s[i] == "D": result += 500
        elif s[i] == "C":
            if i + 1 != len(s) and s[i + 1] in ["D", "M"]:
                result += (400 if s[i + 1] == "D"else 900)
                cont = True
            else: result += 100
        elif s[i] == "L": result += 50
        elif s[i] == "X":
            if i + 1 != len(s) and s[i + 1] in ["L", "C"]:
                result += (40 if s[i + 1] == "L"else 90)
                cont = True
            else: result += 10
        elif s[i] == "V": result += 5
        elif s[i] == "I":
            if i + 1 != len(s) and s[i + 1] in ["V", "X"]:
                result += (4 if s[i + 1] == "V"else 9)
                cont = True
            else: result += 1
    return result

if __name__ == "__main__":
    s = "DCX"
    result = romanToInt(s)
    print(result)
