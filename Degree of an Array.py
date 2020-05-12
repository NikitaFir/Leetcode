class Solution(object):
    def findShortestSubArray(self, nums):

        temp = {}
        k_max = 0
        k_min = 0

        for i in range(0, len(nums)):
            if nums[i] in temp:
                nums[temp[nums[i]]] += 1
                cnt = nums[temp[nums[i]]]
                dis = i - temp[nums[i]]
                if cnt > k_max:
                    k_min = dis
                    k_max = cnt
                elif cnt == k_max and dis < k_min:
                    k_min = dis
            else:
                temp[nums[i]] = i
                nums[i] = 1

        return k_min + 1


print(Solution.findShortestSubArray(0,[1, 2, 2, 3, 1]))
print(Solution.findShortestSubArray(0,[1,2,2,3,1,4,2]))


