class Solution(object):
    def minSubsequence(self, nums):

        k = len(nums) - 1
        i = 0
        j = 0
        nums.sort()

        beg_sum = nums[0]
        end_sum = nums[k]
        result = []
        result.append(nums[k])

        while i + j < len(nums) - 1:

            if beg_sum < end_sum:
                i += 1
                beg_sum += nums[i]

            else:
                k -= 1
                temp = nums[k]
                end_sum += temp
                result.append(temp)
                j += 1

        return result

print(Solution.minSubsequence(0, [4,3,10,9,8]))
print(Solution.minSubsequence(0, [4,4,7,6,7]))


