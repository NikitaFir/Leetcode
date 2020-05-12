class Solution(object):
    def maxScore(self, s):

        n = len(s)
        max_score = 0
        for i in range(1, n):
            left = s[0:i:1]
            right = s[i:n:1]
            temp = left.count("0") + right.count("1")
            if temp > max_score:
                max_score = temp
                
        return max_score