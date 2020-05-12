class Solution(object):
    def createTargetArray(self, nums, index):

        if len(nums) == 1:
            return nums

        result = []
        for i in range(len(index)):
            result.insert(index[i], nums[i])
        return result

print(Solution.createTargetArray(0,[0,1,2,3,4], [0,1,2,2,1]))
print(Solution.createTargetArray(0,[1,2,3,4,0], [0,1,2,3,0]))
print(Solution.createTargetArray(0, [1], [0]))

