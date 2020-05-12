class Solution(object):
    def findPairs(self, nums, i):

        result = 0
        if i == 0:
            temp = {}
            for x in nums:
                if x not in temp:
                    temp[x] = 0
                temp[x] += 1
                if temp[x] == 2:
                    result += 1
        elif i > 0:
            unique = set()
            for x in nums:
                if x not in unique:
                    if (x + i) in unique:
                        result += 1
                    if x - i in unique:
                        result += 1
                    unique.add(x)

        return result

print(Solution.findPairs(0,[3, 1, 4, 1, 5], 2))
