class Solution(object):
    def findSpecialInteger(self, arr):

        count_check = int(0.25 * len(arr))

        for i in range(0,len(arr)):
            if arr.count(arr[i]) > count_check:
                return arr[i]

print(Solution.findSpecialInteger(0,[1,2,2,6,6,6,6,7,10]))
