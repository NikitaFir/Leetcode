import copy
class Solution(object):
    def heightChecker(self, heights):

        students =copy.deepcopy(heights)
        heights.sort()
        move = 0

        for i in range(0, len(heights)):
            if heights[i] != students[i]:
                move += 1

        return move

print(Solution.heightChecker(0,[1,1,4,2,1,3]))
print(Solution.heightChecker(0,[5,1,2,3,4]))
print(Solution.heightChecker(0,[1,2,3,4,5]))