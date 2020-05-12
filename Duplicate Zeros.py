class Solution(object):
    def duplicateZeros(self, arr):

        i = 0
        while i!=len(arr):
            if arr[i]==0:
                arr.insert(i,0)
                arr.pop()
                i+=1
            i+=1
            if i>=len(arr):
                break
        return arr


print(Solution.duplicateZeros(0,[1,0,2,3,0,4,5,0]))
print(Solution.duplicateZeros(0,[1,2,3]))