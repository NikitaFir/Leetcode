class Solution(object):
    def letterCasePermutation(self, S):

        for i in range(0, len(S)):
            S = S[:i] + S[i].lower() + S[i+1:]

        temp = set()
        Solution.helpfunc(self, S, 0, temp)

        ans = [""] * len(temp)
        i = 0
        for s in temp:
            ans[i] = s
            i += 1
        return ans

    def helpfunc(self, s, i, u):
        if i >= len(s):
            u.add(s)
            return

        Solution.helpfunc(self, s, i + 1, u)

        s = s[:i] + s[i].upper() + s[i+1:]

        Solution.helpfunc(self, s, i + 1, u)

print(Solution.letterCasePermutation(0,"a1b2"))

