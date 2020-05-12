class Solution(object):
    def missingNumber(self, nums):

        # сумма массива без пропуска элемента
        n = len(nums)
        sum1 = n*(n+1)/2
        #
        sum2 = 0
        for i in nums:
            sum2 += i
        result = sum1 - sum2

        return result


print(Solution.missingNumber(0,[3,0,1]))
print(Solution.missingNumber(0,[9,6,4,2,3,5,7,0,1]))