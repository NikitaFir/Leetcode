class Solution(object):
    def freqAlphabets(self, s):

        k = 97
        d = {}
        for i in range(1,27):
            if i <= 9:
                d.update({str(i) : chr(k)})
                k += 1
            else:
                d.update({ str(i) + "#" : chr(k)})
                k += 1
        result = ""
        i = 0
        while len(s) != 0:
            if len(s) >= 3:
                if s[i+2] =='#':
                    temp = s[:i] + s[:i + 3]
                    result += d.get(temp)
                    s = s[i + 3:]
                    i = -1
                else:
                    temp = s[i]
                    result += d.get(temp)
                    s = s[i + 1:]
                    i -= 1
            else:
                temp = s[i]
                result += d.get(temp)
                s = s[i + 1:]
                i -= 1

            i += 1
        return result

print(Solution.freqAlphabets(0,"10#11#12"))
print(Solution.freqAlphabets(0,"1326#"))