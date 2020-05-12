class Solution(object):
    def generateTheString(self, n):

        s =""
        if n % 2 != 0:
            for i in range(0,n):
                s +='a'
        else:
            for i in range(0,n - 1):
                s += 'a'
            s += 'b'
        return  s

print(Solution.generateTheString(0,7))