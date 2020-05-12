class Solution(object):
    def isPerfectSquare(self, num):

        if (num**.5).is_integer():
            return True
        else:
            return False

print(Solution.isPerfectSquare(0,16))
print(Solution.isPerfectSquare(0,14))
