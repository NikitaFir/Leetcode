class Solution(object):
    def isOneBitCharacter(self, bits):

        n = len(bits)
        for i in range(0, n):
            if bits[i] == 1 and i + 1 < n:
                bits[i+1] = 2

        return not bits[-1]

print(Solution.isOneBitCharacter(0,[1, 0, 0]))
print(Solution.isOneBitCharacter(0,[1, 1, 1, 0]))



