class Solution(object):
    def canWinNim(self, n):

        if n % 4 != 0:
            return True
        else:
            return False

print(Solution.canWinNim(0,4))

