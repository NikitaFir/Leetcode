class Solution(object):
    def shiftGrid(self, grid, k):

        result = []
        for i in range(0,len(grid)):
            result.append([0] * len(grid[0]))

        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                 c = int((j+k) % len(grid[0]))
                 z = (j+k)/len(grid[0])
                 r = int((i+z) % len(grid))
                 result[r][c] = grid[i][j]

        return result

print(Solution.shiftGrid(0,[[1,2,3],[4,5,6],[7,8,9]], 1))