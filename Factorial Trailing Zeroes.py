class Solution:
    def trailingZeroes(self, n):

        result = 0
        j = 5
        while j <= n:
            result += n//j
            j *= 5
        return result

print(Solution.trailingZeroes(0,3))
print(Solution.trailingZeroes(0,5))
print(Solution.trailingZeroes(0,1808548329))
