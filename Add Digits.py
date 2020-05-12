class Solution(object):
    def addDigits(self, num):

        s = str(num)
        sum = 0
        while num >= 10:
            sum = 0
            for i in range(0,len(s)):
                sum += int(s[i])
            if sum < 10:
                return sum
            else:
                num = sum
                s = str(num)

        return num


print(Solution.addDigits(0,38))
print(Solution.addDigits(0,10))