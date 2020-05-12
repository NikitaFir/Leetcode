class Solution(object):
    def luckyNumbers(self, matrix):

        colmaxs = []
        rowmins = []
        for i in range(0,len(matrix)):
            rowmins.append(min(matrix[i]))

        for i in range(0,len(matrix[i])):
            max = matrix[0][i]
            for j in range(0, len(matrix)):
                if max < matrix[j][i]:
                    max = matrix[j][i]
            colmaxs.append(max)

        result = []
        for i in range(0,len(matrix)):
            for j in range(0, len(matrix[i])):
                if matrix[i][j] == rowmins[i] and matrix[i][j] == colmaxs[j]:
                    result.append(matrix[i][j])

        return result

print(Solution.luckyNumbers(0,[[3,7,8],[9,11,13],[15,16,17]]))
print(Solution.luckyNumbers(0,[[1,10,4,2],[9,3,8,7],[15,16,17,12]]))
print(Solution.luckyNumbers(0,[[7,8],[1,2]]))