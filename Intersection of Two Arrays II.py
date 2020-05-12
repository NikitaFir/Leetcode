class Solution(object):
    def intersect(self, nums1, nums2):

        result = []

        for elem1 in nums1:
            for elem2 in nums2:
                if elem1 == elem2:
                    result.append(elem1)
                    nums2.remove(elem1)
                    break
        return result

print(Solution.intersect(0,[1,2,2,1], [2,2]))
print(Solution.intersect(0,[4,9,5], [9,4,9,8,4]))
print(Solution.intersect(0,[1,2,2,1], [2]))
