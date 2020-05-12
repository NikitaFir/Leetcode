class Solution(object):
    def findLengthOfLCIS(self, nums):

        if len(nums) == 0:
            return 0

        temp = [1]*(len(nums) + 1)

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                temp[i] = 1 + temp[i - 1]
        return max(temp)

print(Solution.findLengthOfLCIS(0,[1,3,5,4,7]))
print(Solution.findLengthOfLCIS(0,[2,2,2,2,2]))
