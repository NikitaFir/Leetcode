class Solution(object):
    def checkStraightLine(self, coordinates):

        k1 = 0
        k2 = 0

        for i in range(0,len(coordinates) - 2):
            try:
                k1 =(coordinates[i][1] - coordinates[i + 1][1])/(coordinates[i][0] - coordinates[i + 1][0])
                k2 = (coordinates[i + 1][1] - coordinates[i + 2][1]) / (coordinates[i + 1][0] - coordinates[i + 2][0])
            except:
                return False

            if k1 != k2:
                return False
        return True

print(Solution.checkStraightLine(0,[[-1,1],[-6,-4],[-6,2],[2,0],[-1,-2],[0,-4]]))
