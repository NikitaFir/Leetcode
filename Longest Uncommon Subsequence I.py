class Solution(object):
    def findLUSlength(self, a, b):

        n = len(a)
        m = len(b)
        if n > m:
            return n
        elif n < m:
            return m
        else:
            if a == b:
                return -1
            else:
                return n

print(Solution.findLUSlength(0,"aba", "cdc"))


