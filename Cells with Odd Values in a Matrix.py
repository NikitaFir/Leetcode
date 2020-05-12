class Solution(object):
    def oddCells(self, n, m, indices):

        # Result = [[0]*m]*n
        t = 0
        Result = [0] * n
        for i in range(n):
            Result[i] = [0] * m

        for i in range(0,len(indices)):
            for j in range(1, len(indices[i])):

                for l in range(0, m):
                    Result[indices[i][j-1]][l] += 1

                for k in range(0, n):
                    Result[k][indices[i][j]] += 1

        for i in range(0,len(Result)):
            for j in range(0, len(Result[i])):
                if Result[i][j] % 2 != 0:
                    t += 1

        return t
print(Solution.oddCells(0,2,3,[[0,1],[1,1]]))
print(Solution.oddCells(0,2,2,[[1,1],[0,0]]))