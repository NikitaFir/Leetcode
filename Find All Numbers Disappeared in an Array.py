class Solution(object):
    def findDisappearedNumbers(self, nums):

        check = []
        for i in range(1,len(nums) + 1):
            check.append(i)

        nums = set(nums)

        if nums == []:

            return []
        else:

            result = list(set(check) - nums)
            return result


print(Solution.findDisappearedNumbers(0,[4,3,2,7,8,2,3,1]))

