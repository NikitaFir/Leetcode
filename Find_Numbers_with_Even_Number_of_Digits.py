class Solution(object):
    def findNumbers(self, nums):

        k = 0
        s =""
        for i in range(0,len(nums)):
            s = str(nums[i])
            if len(s) % 2 == 0:
                k += 1
        return k

print(Solution.findNumbers(0,[12,345,2,6,7896]))
print(Solution.findNumbers(0,[555,901,482,1771]))