class Solution(object):
    def largestTriangleArea(self, points):

        largest_area = 0

        for i in range(0, len(points) - 2):
            for j in range(i + 1, len(points) - 1):
                for k in range(j+1, len(points)):
                    largest_area = max(largest_area, 0.5 * abs(points[i][0] * points[j][1] + points[j][0] * points[k][1] + points[k][0] * points[i][1] - points[i][0] * points[k][1] - points[j][0] * points[i][1] - points[k][0] * points[j][1]))
        return largest_area

print(Solution.largestTriangleArea(0, [[0,0],[0,1],[1,0],[0,2],[2,0]]))

