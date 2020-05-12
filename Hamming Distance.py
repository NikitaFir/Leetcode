class Solution(object):

    def ToBinary(self, x):
        if x == 0:
            return '0'

        res = ''

        while x > 0:
            if x % 2 == 0:
                res = '0' + res
            else:
                res = '1' + res
            x //= 2
        return res

    def hammingDistance(self, x, y):

       x = Solution.ToBinary(self, x)
       y = Solution.ToBinary(self, y)

       result = 0
       i, j = len(x) - 1, len(y) - 1
       while i != -1 and j != -1:
           if x[i] != y[j]:
               result += 1
           i -= 1
           j -= 1

       if i < j:
           while j != -1:
               if y[j] == '1':
                   result += 1
               j -= 1
       else:
           while i != -1:
               if x[i] == '1':
                   result += 1
               i -= 1
       return result

print(Solution.hammingDistance(0,1,4))



