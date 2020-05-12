class Solution(object):
    def hammingWeight(self, n):

        n = bin(n)
        result = n.count('1')
        return result

print(Solution.hammingWeight(0,00000000000000000000000000001011))
