class Solution(object):
    def decompressRLElist(self, nums):

        result = []
        for i in range(0, len(nums) - 1, 2):
            for j in range(0, nums[i]):
               result.append(nums[i + 1])

        return result


print(Solution.decompressRLElist(0,[1,2,3,4]))
print(Solution.decompressRLElist(0,[2,4,4,4]))