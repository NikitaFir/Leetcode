class Solution(object):
    def containsNearbyDuplicate(self, nums, k):

        elems = {}

        for i in range(0, len(nums)):

            if nums[i] in elems:

                value = elems[nums[i]]
                if i - value <= k:
                    return True
                else:
                    elems[nums[i]] = i

            else:
                elems.update({nums[i]: i})

        return False

print(Solution.containsNearbyDuplicate(0,[1,2,3,1], 3))
print(Solution.containsNearbyDuplicate(0,[1,0,1,1], 1))
print(Solution.containsNearbyDuplicate(0,[1,2,3,1,2,3], 2))