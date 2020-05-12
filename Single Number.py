class Solution(object):
    def singleNumber(self, nums):

        SingleDigits = set(nums)
        result = sum(SingleDigits)*2 - sum(nums)
        return result
    
print(Solution.singleNumber(0,[4,1,2,1,2]))