class Solution(object):
    def prefixesDivBy5(self, A):

        temp = ""
        result = []

        for i in range(0, len(A)):
            temp += str(A[i])
            if int(temp, 2) % 5 == 0:
                result.append(True)
            else:
                result.append(False)

        return result
print(Solution.prefixesDivBy5(0,[0,1,1]))
print(Solution.prefixesDivBy5(0,[1,1,1]))
print(Solution.prefixesDivBy5(0,[1,1,1,0,1]))
