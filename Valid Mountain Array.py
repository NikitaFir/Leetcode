class Solution(object):
    def validMountainArray(self, A):

        if len(A) < 3:
            return False
        x = A[1] - A[0]
        if x <= 0:
            return False
        for i in range(2, len(A)):
            y = A[i] - A[i - 1]
            if y == 0:
                 return False
            if x < 0 and y > 0:
                return False
            x = y

        return x < 0

print(Solution.validMountainArray(0,[0,3,2,1]))


