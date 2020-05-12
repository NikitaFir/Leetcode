class Solution:
    def largestPerimeter(self, A):

        result = 0
        A.sort()

        for i in range(len(A) - 1, 1, -1):

            if A[i - 2] + A[i - 1] > A[i]:
                result = A[i - 2] + A[i - 1] + A[i]
                return result

        return result

print(Solution.largestPerimeter(0,[3,6,2,3]))