class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):

        result = 0

        for i in range(len(arr1)):
            for j in range(len(arr2)):
                if abs(arr1[i]-arr2[j]) <= d:
                    result += 1
                    break

        result = len(arr1) - result

        return result

print(Solution.findTheDistanceValue(0,[4,5,8],[10,9,1,8], 2))
print(Solution.findTheDistanceValue(0,[1,4,2,3],[-4,-3,6,10,20,30], 3))
print(Solution.findTheDistanceValue(0, [2,1,100,3],[-5,-2,10,-3,7], 6))


