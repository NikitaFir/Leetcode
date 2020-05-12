class Solution(object):
    def reverse(self, x):
        if (x >-2147483648 and x < 2147483648):
            s =''
            if x < 0:
                x *= -1
                s = str(x)
                s = s[::-1]
                s = '-' + s
                x = int(s)
            else:
                s = str(x)
                s = s[::-1]
                x = int(s)
        else:
            return 0
        return x

print(Solution.reverse(0,1534236469))
print(Solution.reverse(0,-1233))