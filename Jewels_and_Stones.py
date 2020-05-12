class Solution(object):
    def numJewelsInStones(self, J, S):

        k = 0
        for i in range(0,len(J)):
            for j in range(0,len(S)):
                if J[i] == S[j]:
                    k += 1
        return k

print(Solution.numJewelsInStones(0,"aA","aAAbbbb"))
print(Solution.numJewelsInStones(0,"z","ZZ"))