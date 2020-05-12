class Solution(object):
    def minStartValue(self, nums):

        result = 1
        Sum = 1

        for i in range(0, len(nums)):
            Sum += nums[i]

            if Sum < 1:
                result += 1 - Sum
                Sum = 1

        return result


print(Solution.minStartValue(0,[-3,2,-3,4,2]))
