class Solution(object):
    def rob(self, nums):

        prev = 0
        now = 0

        for money in nums:
            score = max(now, money + prev)
            prev = now
            now = score

        return now

print(Solution.rob(0,[1,2,3,1]))
print(Solution.rob(0,[2,7,9,3,1]))
print(Solution.rob(0,[1,2]))
print(Solution.rob(0,[]))