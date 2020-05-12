class Solution(object):
    def dominantIndex(self, nums):

        j = 0

        for i in range(0,len(nums)):
            if nums[i] > nums[j]:
                j = i

        for i in range(0, len(nums)):
            if j != i and nums[j] < (2 * nums[i]):
                return -1

        return j

print(Solution.dominantIndex(0,[3, 6, 1, 0]))
print(Solution.dominantIndex(0,[1, 2, 3, 4]))
print(Solution.dominantIndex(0,[0,0,0,1]))