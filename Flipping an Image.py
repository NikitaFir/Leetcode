class Solution(object):
    def flipAndInvertImage(self, A):

        for i  in range(0,len(A)):
            A[i].reverse()

        for i in range(0, len(A)):
            for j in range(0,len(A[i])):
                if A[i][j]==1:
                    A[i][j]=0
                elif A[i][j]==0:
                    A[i][j]=1

        return A

print(Solution.flipAndInvertImage(0,[[1,1,0],[1,0,1],[0,0,0]]))
print(Solution.flipAndInvertImage(0,[[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))