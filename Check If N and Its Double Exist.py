class Solution(object):
    def checkIfExist(self, arr):

        result = set()
        for i in arr:
            if (i * 2 in result) or (i % 2 == 0 and i // 2 in result):
                return True
            result.add(i)
        return False

print(Solution.checkIfExist(0,[3,1,7,11]))
