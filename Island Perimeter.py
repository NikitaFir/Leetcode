class Solution(object):
    def islandPerimeter(self, grid):

        if grid == [] or grid[0] == []:
            return 0

        perimeter = 0

        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 1:
                    if i == 0:
                        perimeter += 1
                    if i == len(grid) - 1:
                        perimeter += 1
                    if i - 1 >= 0 and grid[i - 1][j] == 0:
                        perimeter += 1
                    if i + 1 < len(grid) and grid[i + 1][j] == 0:
                        perimeter += 1
                    if j == 0:
                        perimeter += 1
                    if j == len(grid[0]) - 1:
                        perimeter += 1
                    if j - 1 >= 0 and grid[i][j - 1] == 0:
                        perimeter += 1
                    if j + 1 < len(grid[0]) and grid[i][j + 1] == 0:
                        perimeter += 1
        return perimeter

print(Solution.islandPerimeter(0,[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))
