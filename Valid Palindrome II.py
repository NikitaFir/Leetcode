class Solution(object):

    def Check(self, s, i, j):
        while j > i:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True

    def validPalindrome(self, s):

        L = len(s)

        for i in range(0, L):
            if s[i] != s[L - i - 1]:
                j = L - i - 1
                return Solution.Check(self, s, i + 1, j) or Solution.Check(self, s, i, j - 1)
        return True

print(Solution.validPalindrome(0,"aba"))
print(Solution.validPalindrome(0,"abca"))



