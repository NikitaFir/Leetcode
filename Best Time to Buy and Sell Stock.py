class Solution(object):
    def maxProfit(self, prices):

        if len(prices) == 0:
            return 0

        result = 0
        price = prices[0]

        for i in range(1, len(prices)):
            price = min(price, prices[i])
            result = min(result, price - prices[i])

        return abs(result)

print(Solution.maxProfit(0, [7,1,5,3,6,4]))



