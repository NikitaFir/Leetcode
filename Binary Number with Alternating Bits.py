class Solution(object):
    def hasAlternatingBits(self, n):

        Bin = bin(n)
        Bin = Bin[2:]

        for i in range(0,len(Bin) - 1):
            if Bin[i] == Bin[i + 1]:
                return False

        return True

print(Solution.hasAlternatingBits(0, 5))
print(Solution.hasAlternatingBits(0, 7))
print(Solution.hasAlternatingBits(0, 11))
print(Solution.hasAlternatingBits(0, 10))
