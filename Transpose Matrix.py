class Solution(object):
    def transpose(self, A):

        n = len(A)
        m = len(A[n-1])
        temp = [0]*m

        for i in range(0,m):
            temp[i] = [0] * n

        for i in range(0, m):
            for j in range(0, n):
                temp[i][j]=A[j][i]

        return temp

print(Solution.transpose(0,[[1,2,3],[4,5,6],[7,8,9]]))
print(Solution.transpose(0,[[1,2,3],[4,5,6]]))