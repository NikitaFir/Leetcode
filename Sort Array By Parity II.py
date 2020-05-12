class Solution(object):
    def sortArrayByParityII(self, A):

        even,odd,result =[],[],[]

        for digit in A:
            if digit % 2 == 0:
                even.append(digit)
            else:
                odd.append(digit)

        for i,j in zip(even,odd):
            result.append(i)
            result.append(j)

        return result

print(Solution.sortArrayByParityII(0,[4,2,5,7]))