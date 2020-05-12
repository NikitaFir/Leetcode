class Solution(object):
    def moveZeroes(self, nums):

        temp = 0
        flag = False
        while True:
            flag = False
            for i in range(len(nums)-1, 0, -1):
                if nums[i] != 0 and nums[i-1] == 0:
                    temp = nums[i]
                    nums[i] = nums[i-1]
                    nums[i-1] = temp
                    flag = True
            if not flag:
                break

print(Solution.moveZeroes(0,[0,1,0,3,12]))