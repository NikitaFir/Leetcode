class Solution(object):
    def distributeCandies(self, candies):

        unique = set(candies)
        L1 = len(candies)
        L2 = len(unique)

        if L2 >= L1 // 2:
            return L1 // 2
        else:
            return L2

print(Solution.distributeCandies(0,[1,1,2,2,3,3]))
print(Solution.distributeCandies(0,[1,1,2,3]))
