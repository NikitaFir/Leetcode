class Solution(object):
    def commonChars(self, A):
        result = []
        temp = []

        for i in range(0,len(A)):
            temp = list(A[i])
            for j in range(0,len(temp)):
                k = 0
                for l in range(i+1,len(A)):
                    if A[l].find(temp[j]) != -1:
                        t = A[l].find(temp[j])
                        A[l]=A[l][:t] + A[l][t+1:]
                        k+=1
                if k == len(A) - 1:
                    result.append(temp[j])

        return result

print(Solution.commonChars(0,["bella","label","roller"]))
print(Solution.commonChars(0,["cool","lock","cook"]))