class Solution(object):
    def containsDuplicate(self, nums):

        NoDuplicates = set(nums)

        if len(nums) == len(NoDuplicates):
            return False
        else:
            return True

print(Solution.containsDuplicate(0,[1,2,3,1]))
print(Solution.containsDuplicate(0,[1,2,3,4]))
print(Solution.containsDuplicate(0,[1,1,1,3,3,4,3,2,4,2]))