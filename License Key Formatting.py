class Solution(object):
    def licenseKeyFormatting(self, S, K):

        temp = ""
        counter = 0
        for i in range(len(S)-1, -1, -1):
            if S[i] != '-':
                if counter > 0 and counter % K == 0:
                    temp += '-'
                temp += S[i].upper()
                counter += 1

        ch = list(str(temp))
        ch.reverse()
        return ''.join(ch)


print(Solution.licenseKeyFormatting(0,"5F3Z-2e-9-w", 4))
print(Solution.licenseKeyFormatting(0,"2-5g-3-J", 2))

