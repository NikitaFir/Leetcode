class Solution(object):
    def detectCapitalUse(self, word):

        if word.islower():
            return True
        elif word.isupper():
            return True

        S1 = word[:1]
        S2 = word[1:]

        if S1.isupper() and S2.islower():
            return True

        return False
    
print(Solution. detectCapitalUse(0,"USA"))
print(Solution. detectCapitalUse(0,"FlaG"))
print(Solution. detectCapitalUse(0,"Leetcode"))