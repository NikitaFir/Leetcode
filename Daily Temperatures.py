class Solution(object):
    def dailyTemperatures(self, T):

        result = [0] * len(T)
        temp = []
        for i in range(0, len(T)):
            while len(temp) != 0 and T[temp[-1]] < T[i]:
                j = temp.pop()
                result[j] = i - j
            temp.append(i)

        return result

print(Solution.dailyTemperatures(0, [73, 74, 75, 71, 69, 72, 76, 73]))
