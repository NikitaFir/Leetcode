class Solution(object):
    def checkPossibility(self, nums):

        if len(nums) <= 2:
            return 1
        K1 = 0
        K2 = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if nums[i] > K1:
                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]
                K2 += 1
            K1 = nums[i - 1]

        if K2 <= 1:
            return True
        else:
            return False

print(Solution.checkPossibility(0,[4,2,3]))
print(Solution.checkPossibility(0,[4,2,1]))