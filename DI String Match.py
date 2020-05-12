class Solution(object):
    def diStringMatch(self, S):

        n = len(S)
        inc = -1
        dec = n + 1
        result = []
        for i in range(0,n):
            if S[i] == 'D':
                dec -= 1
                result.append(dec)
            elif S[i] =='I':
                inc += 1
                result.append(inc)
        if S[-1] == 'I':
            inc += 1
            result.append(inc)
        elif S[-1] == 'D':
            dec -= 1
            result.append(dec)
        return result

print(Solution.diStringMatch(0,"IDID"))
print(Solution.diStringMatch(0,"III"))
print(Solution.diStringMatch(0,"DDI"))
