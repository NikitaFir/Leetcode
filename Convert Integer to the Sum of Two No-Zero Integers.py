class Solution(object):
    def getNoZeroIntegers(self, n):

        result = []
        beg = n
        while True:
            n -= 1
            x, y = n, beg - n
            if (not '0' in (str(x))) and (not '0' in (str(y))):
                break

        result.append(y)
        result.append(x)

        return result

print(Solution.getNoZeroIntegers(0,2))
print(Solution.getNoZeroIntegers(0,11))
print(Solution.getNoZeroIntegers(0,10000))
print(Solution.getNoZeroIntegers(0,69))
print(Solution.getNoZeroIntegers(0,1010))
print(Solution.getNoZeroIntegers(0,4102))