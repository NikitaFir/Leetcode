class Solution(object):
    def nextGreaterElement(self, nums1, nums2):

        temp =[]
        dict = {}

        for i in range(0, len(nums2)):
            while len(temp) != 0 and nums2[i] > temp[-1]:
                dict[temp[-1]] = nums2[i]
                temp.pop()

            temp.append(nums2[i])

        while len(temp) != 0:

            dict[temp[-1]] = -1
            temp.pop()


        result =  []
        for i in range(0, len(nums1)):
            result.append(dict[nums1[i]])

        return result

print(Solution.nextGreaterElement(0, [4,1,2], [1,3,4,2]))
print(Solution.nextGreaterElement(0, [2,4], [1,2,3,4]))


