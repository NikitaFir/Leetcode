class Solution(object):
    def minTimeToVisitAllPoints(self, points):

        time = 0
        for i in range(len(points) - 1):
            time += max(abs(points[i + 1][0] - points[i][0]), abs(points[i + 1][1] - points[i][1]))
        return time

print(Solution.minTimeToVisitAllPoints(0,[[1,1],[3,4],[-1,0]]))
print(Solution.minTimeToVisitAllPoints(0,[[3,2],[-2,2]]))


