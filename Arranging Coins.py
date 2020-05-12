class Solution(object):
    def arrangeCoins(self, n):

        coins = n
        row = 0

        k = 1
        while k <= coins:
            row += 1
            coins -= k
            k += 1
        return row

print(Solution.arrangeCoins(0,5))
print(Solution.arrangeCoins(0,8))
