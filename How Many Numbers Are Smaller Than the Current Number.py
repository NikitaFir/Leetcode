class Solution(object):
    def smallerNumbersThanCurrent(self, nums):

        result = []
        for i in range(0,len(nums)):
            k = 0
            for j in range(0, len(nums)):
                if nums[i] > nums[j] and i != j:
                    k += 1
            result.append(k)
        return  result

print(Solution.smallerNumbersThanCurrent(0,[8,1,2,2,3]))
print(Solution.smallerNumbersThanCurrent(0,[7,7,7,7]))