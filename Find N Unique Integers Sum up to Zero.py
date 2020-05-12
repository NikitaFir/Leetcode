class Solution(object):
    def sumZero(self, n):

        result = []


        for i in range(-(n // 2), (n // 2) + 1):
            result.append(i)

        if  n % 2 ==0:
            del result[len(result) // 2]

        return result
print(Solution.sumZero(0,5))
print(Solution.sumZero(0, 3))
