class Solution(object):
    def isMonotonic(self, A):

        i = 0
        fl = True
        while fl and i!=len(A) - 1:
            if A[i] <= A[i + 1]:
                i += 1
            else:
                fl = False

        if i == len(A) - 1:
            return fl

        i = 0
        fl = True
        while fl and i != len(A) - 1:
            if A[i] >= A[i + 1]:
                i += 1
            else:
                fl = False
        return fl


print(Solution.isMonotonic(0,[1,2,2,3]))
print(Solution.isMonotonic(0,[6,5,4,4]))
print(Solution.isMonotonic(0,[1,3,2]))
print(Solution.isMonotonic(0,[1,2,4,5]))
print(Solution.isMonotonic(0,[1,1,1]))
