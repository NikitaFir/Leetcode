class Solution(object):
    def isSubsequence(self, s, t):

        if s == "" or not s:
             return True

        if len(t) < len(s):
            return False

        if s == t:
            return True

        k = 0
        s = list(s)

        for elem in t:
            if s[k] == elem:
                k += 1
                if k == len(s):
                    return True
        return False

print(Solution.isSubsequence(0,"abc", "ahbgdc"))
print(Solution.isSubsequence(0,"", "ahbgdc"))