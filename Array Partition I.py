class Solution(object):
    def arrayPairSum(self, nums):

        nums.sort()
        m = []
        result = []
        for i in range(0,len(nums) - 1,2):
            m.append(nums[i])
            m.append(nums[i+1])
            result.append(m[:])
            del m[:]
        sum = 0
        for i in range(0, len(result)):
            sum+=min(result[i])

        return sum

print(Solution.arrayPairSum(0,[1,4,3,2]))