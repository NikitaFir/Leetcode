class Solution(object):
    def isHappy(self, n):

        while n != 1 and n != 7:
            if n % 10 == n:
                return False
            k = 0
            while n != 0:
                k = k + (n % 10) * (n % 10)
                n /= 10
            n = k
        return True

print(Solution.isHappy(0,1))
