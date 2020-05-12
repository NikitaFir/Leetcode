class Solution(object):
    def firstUniqChar(self, s):

        repeatedchars = {}

        for alf in s:
            if alf in repeatedchars:
                repeatedchars[alf] += 1
            else:
                repeatedchars[alf] = 1


        for i in range(0, len(s)):
            if repeatedchars[s[i]] == 1:
                return i

        return -1

print(Solution.firstUniqChar(0, "leetcode"))
print(Solution.firstUniqChar(0, "loveleetcode"))


