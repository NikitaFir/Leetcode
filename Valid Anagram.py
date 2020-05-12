class Solution(object):
    def isAnagram(self, s, t):

        check = {}

        for i in s:
            if i not in check:
                check[i] = 1
            else:
                check[i] += 1

        for i in t:
            if i not in check:
                return False
            else:
                check[i] -= 1

        for key in check:
            if check[key] != 0:
                return False

        return True

print(Solution.isAnagram(0,"anagram", "nagaram"))
print(Solution.isAnagram(0,"rat","car"))