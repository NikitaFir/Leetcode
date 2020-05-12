class Solution(object):
    def countPrimes(self, n):

        result = 0
        temp = [1]*n

        for i in range(2, n):
            if temp[i] == 1:
                result += 1
                k = 2
                c = i

                while c * k < n:
                    temp[c * k] = 0
                    k += 1
        return result

print(Solution.IsPrime(0,10))