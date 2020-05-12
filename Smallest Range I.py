class Solution(object):
    def smallestRangeI(self, A, K):

        result = 0
        MIN = min(A)
        MAX = max(A)

        if (MIN + K) < (MAX - K):
            result = (MAX - K) - (MIN + K)
            return result

        if (MIN + K) >= (MAX - K):
            return result

print(Solution.smallestRangeI(0,[0,10],2))
print(Solution.smallestRangeI(0,[1,3,6],3))
