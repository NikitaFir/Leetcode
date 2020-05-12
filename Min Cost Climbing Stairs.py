class Solution(object):
    def minCostClimbingStairs(self, cost):

        x = 0
        y = 0
        for i in range(len(cost)-1, -1, -1):
            z = cost[i] + min(y, x)
            y = x
            x = z

        return min(y, x)


print(Solution.minCostClimbingStairs(0,[10, 15, 20]))
print(Solution.minCostClimbingStairs(0,[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))