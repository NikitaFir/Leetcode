class Solution(object):
    def twoSum(self, nums, target):
        result = []
        for i in range(0,len(nums)):
            for j in range(i + 1, len(nums)):
                Sum = nums[i] + nums[j]
                if Sum == target:
                    result.append(i)
                    result.append(j)
                    return result

l = [2, 7, 11, 15]
target = 9
print(Solution.twoSum(0,l,target))