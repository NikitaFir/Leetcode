class Solution(object):
    def climbStairs(self, n):

        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 3

        x = 2
        y = 3
        result = 0
        for i in range(4, n + 1):
            result = x + y
            x = y
            y = result
        return result

print(Solution.climbStairs(0, 7))
