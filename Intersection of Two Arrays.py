class Solution(object):
    def intersection(self, nums1, nums2):

        nums1 = set(nums1)
        nums2 = set(nums2)
        result = list(nums1.intersection(nums2))

        return result
    
print(Solution.intersection(0,[1,2,2,1],[2,2]))
print(Solution.intersection(0,[4,9,5],[9,4,9,8,4]))
