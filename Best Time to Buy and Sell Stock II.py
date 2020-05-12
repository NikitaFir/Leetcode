class Solution(object):
    def maxProfit(self, prices):

        profit = 0

        for i in range(len(prices)-1):
            difference = prices[i+1] - prices[i]
            if difference > 0:
                profit += difference

        return profit

print(Solution.maxProfit(0, [7,1,5,3,6,4]))


