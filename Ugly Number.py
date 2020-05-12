class Solution(object):
    def isUgly(self, num):

        if num == 1 or num == 2 or num == 3 or num == 5:
            return True
        else:
            # разложение числа на простые множители
            result = []
            k = 2
            while k * k <= num:
                if num % k == 0:
                    result.append(k)
                    num //= k
                else:
                    k += 1
            if num > 1:
                result.append(num)
            if not result:
                return False
            elif result[-1] == 2 or result[-1] == 3 or result[-1] == 5:
                return True
            else:
                return False

print(Solution.isUgly(0,6))
print(Solution.isUgly(0,8))
print(Solution.isUgly(0,14))
print(Solution.isUgly(0,1))