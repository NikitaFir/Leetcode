class Solution(object):
    def findJudge(self, N, trust):

        temp = [0] * (N + 1)
        for i in range(0, len(trust)):
            temp[trust[i][1]] += 1
            temp[trust[i][0]] = -1
        for i in range(1, N + 1):
            if temp[i] == N - 1:
                return i
        return -1

print(Solution.findJudge(0,4,[[1,3],[2,3],[3,1]]))
print(Solution.findJudge(0,3,[[1,3],[2,3],[3,1]]))
