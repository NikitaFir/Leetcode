class Solution(object):
    def maxNumberOfBalloons(self, text):

        b = 0
        a = 0
        l = 0
        o = 0
        n = 0
        for i in range(0,len(text)):
            if text[i] == 'b':
                b += 1
            elif text[i] == 'a':
                a += 1
            elif text[i] == 'l':
                l += 1
            elif text[i] == 'o':
                o += 1
            elif text[i] == 'n':
                n += 1
        l //= 2
        o //= 2
        amount =[b,a,l,o,n]
        result = min(amount)
        return result

print(Solution.maxNumberOfBalloons(0,"nlaebolko"))
print(Solution.maxNumberOfBalloons(0,"loonbalxballpoon"))