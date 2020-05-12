class Solution(object):
    def findMaxConsecutiveOnes(self, nums):

        for i in range(0,len(nums)):
            nums[i] = str(nums[i])

        s =''.join(nums)
        ones = s.split('0')

        L = []

        for i in range(0,len(ones)):
            L.append(len(ones[i]))

        return max(L)




print(Solution.findMaxConsecutiveOnes(0,[1,1,0,1,1,1]))
