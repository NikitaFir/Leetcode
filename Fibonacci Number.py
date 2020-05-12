class Solution(object):
    def fib(self, N):

        if N == 0:
            return 0
        elif N == 1:
            return 1
        else:
            return Solution.fib(self,N - 1) + Solution.fib(self,N - 2)

print(Solution.fib(0,30))