class Solution(object):
    def repeatedNTimes(self, A):

        k = 0
        for i in range(0,len(A)):
            k = 0
            for j in range(0,len(A)):
                if A[i] == A[j]:
                    k += 1
                    if k == len(A)/2:
                        return A[i]

print(Solution.repeatedNTimes(0,[1,2,3,3]))
print(Solution.repeatedNTimes(0,[2,1,2,5,3,2]))
print(Solution.repeatedNTimes(0,[5,1,5,2,5,3,5,4]))