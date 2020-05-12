class Solution(object):
    def tribonacci(self, n):

        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            triboc = [0, 1, 1]
            for i in range(2, n):
                triboc.append(triboc[-1] + triboc[-2] + triboc[-3])

        return triboc.pop()

print(Solution.tribonacci(0, 25))
