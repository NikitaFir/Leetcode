class Solution(object):
    def lengthOfLastWord(self, s):

        if s =="":
            return 0
        temp =s.split(' ')

        while len(temp) != 0:
            word = temp.pop()
            if word !="":
                return  len(word)
        return 0

print(Solution.lengthOfLastWord(0,"Hello World"))
print(Solution.lengthOfLastWord(0,"a "))
print(Solution.lengthOfLastWord(0,""))