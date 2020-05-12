class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):

        result = []
        max_val = max(candies)
        for i in range(0,len(candies)):
            if candies[i] + extraCandies >= max_val:
                result.append(True)
            else:
                result.append(False)
        return result


print(Solution.kidsWithCandies(0,[2,3,5,1,3], 3))
