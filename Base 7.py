class Solution(object):
    def convertToBase7(self, num):

        result =""

        if num == 0:
            return "0"

        if num < 0:
            fl = True
            num *= -1
        else:
            fl = False


        while num > 0:
            temp = num % 7
            num //= 7
            result = str(temp) + result

        if fl:
            result ="-" + result

        return result

# print(Solution. convertToBase7(0,100))
print(Solution. convertToBase7(0,-7))
print(Solution. convertToBase7(0,0))

