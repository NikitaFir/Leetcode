class Solution(object):
    def findContentChildren(self, g, s):

        result = 0
        i = len(g) - 1
        j = len(s) - 1
        g.sort()
        s.sort()
        while i >= 0 and j >= 0:
            if g[i] > s[j]:
                i -= 1
            else:
                if g[i] <= s[j]:
                    i -= 1
                    j -= 1
                    result += 1

        return result

print(Solution.findContentChildren(0,[1,2,3], [1,1]))
print(Solution.findContentChildren(0,[1,2], [1,2,3]))
