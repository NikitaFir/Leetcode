class Solution(object):
    def delims(self, delim, str):

        if len(str) % len(delim) != 0:
            return False
        size = len(delim)
        for i in range(0, len(str), size):
            y = str[i:i + size:1]
            if delim != y:
                return False
        return True

    def gcdOfStrings(self, str1, str2):

        if len(str1) < len(str2):
            a = str1
            b = str2
        else:
            a = str2
            b = str1
        for i in range(len(a), 0, -1):
            x = a[:i]
            if Solution.delims(self, x, b) and Solution.delims(self, x, a):
                return x
        return ""

print(Solution.gcdOfStrings(0,"ABCABC", "ABC"))
print(Solution.gcdOfStrings(0,"ABABAB", "ABAB"))
print(Solution.gcdOfStrings(0,"LEET", "CODE"))
