class Solution(object):
    def countNegatives(self, grid):

        k = 0
        for i in range(0,len(grid)):
            for j in range(0,len(grid[i])):
                if grid[i][j] < 0:
                    k+=1
        return k

print(Solution.countNegatives(0,[[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))
print(Solution.countNegatives(0,[[3,2],[1,0]]))
print(Solution.countNegatives(0,[[1,-1],[-1,-1]]))
print(Solution.countNegatives(0,[[-1]]))