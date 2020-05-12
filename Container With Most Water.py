class Solution(object):
    def maxArea(self, height):

        result = 0
        k1 = 0
        k2 = len(height) - 1
        while k1 < k2:
            result = max(result, (min(height[k1], height[k2]) * (k2 - k1)))

            if height[k1] < height[k2]:
                k1 += 1
            else:
                k2 -= 1
        return result

print(Solution.maxArea(0,[1,8,6,2,5,4,8,3,7]))
