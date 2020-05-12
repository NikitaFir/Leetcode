class Solution(object):
    def maximum69Number (self, num):

        s = str(num)
        fl = True
        i = 0
        while fl and i != len(s) :
            if s[i] =='6':
                s = s[:i] + '9' + s[i+1:]
                num = int(s)
                fl = False
            i += 1
        return num


print(Solution.maximum69Number(0,9669))
print(Solution.maximum69Number(0,9996))
print(Solution.maximum69Number(0,9999))