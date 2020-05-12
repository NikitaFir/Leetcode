class Solution(object):
    def GetDigits(self, s):

        l = len(s)
        digit = []
        i = 0
        while i < l:
            temp = ''
            a = s[i]
            while '0' <= a <= '9' or a =='-':
                temp += a
                i += 1
                if i < l:
                    a = s[i]
                else:
                    break
            i += 1
            if temp != '':
                digit.append(int(temp))
        return  digit
    def complexNumberMultiply(self, a, b):

        digit1,digit2 =Solution.GetDigits(self, a),Solution.GetDigits(self, b)

        C1 = complex(digit1[0],digit1[1])
        C2 = complex(digit2[0], digit2[1])
        C3 = C1 * C2
        result = str(C3)
        if C3.real == 0 and (C3.imag >= 0 or C3.imag <= 0):
            result = "0+" + result
        elif C3.imag < 0:
            k = result.find('-',2,len(result))
            result = result[:k] + '+' + result[k:]
        result = result.replace('j','i')
        result = result.replace('(','')
        result = result.replace(')', '')
        return result

print(Solution.complexNumberMultiply(0, "1+1i", "1+1i"))
print(Solution.complexNumberMultiply(0, "1+-1i", "1+-1i"))
print(Solution.complexNumberMultiply(0, "1+0i", "1+0i"))
print(Solution.complexNumberMultiply(0, "1+-1i", "0+0i"))
print(Solution.complexNumberMultiply(0, "20+22i", "-18+-10i"))