class Solution(object):
    def bitwiseComplement(self, N):

        N = bin(N)[2:]

        for i in range(0,len(N)):
            if N[i] == '1':
                N = N[:i] + '0' + N[i+1:]
            else:
                N = N[:i] + '1' + N[i + 1:]

        N = int(N, 2)

        return N
print(Solution.bitwiseComplement(0,5))
print(Solution.bitwiseComplement(0,7))
print(Solution.bitwiseComplement(0,10))