class Solution(object):
    def majorityElement(self, nums):

        elems = {}
        for elem in nums:
            if elem in elems:
                elems[elem] += 1
            else:
                elems[elem] = 1

        for key, value in elems.items():
            if value == max(elems.values()):
                return key

print(Solution.majorityElement(0,[3,2,3,4,4,4]))
print(Solution.majorityElement(0,[3,3,4]))