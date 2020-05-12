class Solution(object):
    def pivotIndex(self, nums):

        left = [0] * len(nums)
        right = [0] * len(nums)

        left_sum = 0
        for i in range(0, len(nums)):
            left_sum += nums[i]
            left[i] = left_sum

        right_sum = 0
        for i in range(len(nums) - 1, -1, -1):
            right_sum += nums[i]
            right[i] = right_sum

        for i in range(0, len(nums)):
            if left[i] == right[i]:
                return i
        return -1

print(Solution.pivotIndex(0,[1, 7, 3, 6, 5, 6]))
print(Solution.pivotIndex(0,[1, 2, 3]))
print(Solution.pivotIndex(0,[-1,-1,-1,-1,0,1]))
print(Solution.pivotIndex(0,[-1,-1,-1,0,1,1]))