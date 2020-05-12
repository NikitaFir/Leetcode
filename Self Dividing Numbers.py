class Solution(object):
    def selfDividingNumbers(self, left, right):

        Result = []

        for i in range(left,right + 1):
            k = 0
            s = str(i)
            for j in range(0,len(s)):
                if int(s[j])!=0:
                    if i % int(s[j])==0:
                        k+=1

            if k==len(s):
                Result.append(i)

        return Result

print(Solution.selfDividingNumbers(0,1,22))