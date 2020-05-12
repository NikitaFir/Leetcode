class Solution(object):
    def findTheDifference(self, s, t):

        S1 = 0
        S2 = 0

        for i in range(0,len(s)):
            S1 += ord(s[i])
        for i in range(0, len(t)):
            S2 += ord(t[i])
        result = str(chr(S2-S1))

        return result

print(Solution.findTheDifference(0,"abcd","abcde"))
