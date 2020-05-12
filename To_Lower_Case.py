class Solution(object):
    def toLowerCase(self, str):

        if str.islower():
            return  str
        else:
            return str.lower()


print(Solution.toLowerCase(0,"Hello"))
print(Solution.toLowerCase(0,"here"))
print(Solution.toLowerCase(0,"LOVELY"))