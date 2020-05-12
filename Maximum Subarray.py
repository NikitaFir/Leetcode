class Solution(object):
    def maxSubArray(self, nums):

        temp = []
        temp.append(nums[0])
        max = temp[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i] + temp[i - 1]:
                temp.append(nums[i])
            else:
                temp.append(nums[i] + temp[i-1])
            if temp[i] > max:
                max = temp[i]

        return max

print(Solution.maxSubArray(0,[-2,1,-3,4,-1,2,1,-5,4]))


