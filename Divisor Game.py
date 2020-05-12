class Solution(object):
    def divisorGame(self, N):
        k = 0
        x = 1
        while N != x:
            if N % x==0:
                k += 1
                N -= x
                x = 1
            else:
                x += 1
        if k % 2 != 0:
            return True
        else:
            return False
print(Solution.divisorGame(0,3))