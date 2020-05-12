class Solution(object):
    def isValid(self, s):

        length = len(s)
        i = 1
        while length != i and length != 0:
            if s[i-1] =='(' and s[i] == ')':
                s = s[:i - 1] + s[i:]
                s = s[:i - 1] + s[i:]
                length = len(s)
                i = 0
            elif s[i-1] == '{' and s[i] == '}':
                s = s[:i - 1] + s[i:]
                s = s[:i - 1] + s[i:]
                length = len(s)
                i = 0
            elif s[i-1] == '[' and s[i] == ']':
                s = s[:i - 1] + s[i:]
                s = s[:i - 1] + s[i:]
                length = len(s)
                i = 0
            i += 1
        if length == 0:
            return True
        else:
            return False

print(Solution.isValid(0,"()"))
print(Solution.isValid(0,"(){[}]{}"))
print(Solution.isValid(0,"(]"))
print(Solution.isValid(0,"([)]"))