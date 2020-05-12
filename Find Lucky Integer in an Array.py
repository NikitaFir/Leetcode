class Solution(object):
    def findLucky(self, arr):

        result = -1

        for i in range(0,len(arr)):
            if arr.count(arr[i]) == arr[i] and arr[i] > result:
                result = arr[i]
        return result

print(Solution.findLucky(0,[2,2,3,4]))
print(Solution.findLucky(0,[7,7,7,7,7,7,7]))

