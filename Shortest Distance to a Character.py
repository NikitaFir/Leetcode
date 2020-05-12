class Solution(object):
    def shortestToChar(self, S, C):

        temp = []
        result = []

        for i in range(0, len(S)):
            if S[i] == C:
                temp.append(i)

        if len(temp) == 1:
            for i in range(0, len(S)):
                result.append(abs(i - temp[0]))
            return result

        j = 0

        for i in range(0, len(S)):
            k1 = abs(i - temp[j])
            k2 = abs(i - temp[j+1])

            if k1 <= k2:
                result.append(k1)
            elif k1 > k2:
                result.append(k2)

            if k2 == 0 and j + 1 < len(temp) - 1:
                j += 1

        return result

print(Solution.shortestToChar(0,"loveleetcode", 'e'))