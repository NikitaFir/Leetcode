class Solution(object):
    def sortString(self, s):

        beginlen = len(s)
        temp = s
        result = ""
        while len(result) != beginlen:
            while len(temp) != 0:
                elem_one = min(list(temp))
                temp = temp.replace(elem_one,'')
                index = s.find(elem_one)
                s = s[:index] + s[index + 1:]
                result += elem_one
            if len(result) == beginlen:
                break
            temp = s
            while len(temp) != 0:
                elem_one = max(list(temp))
                temp = temp.replace(elem_one, '')
                index = s.find(elem_one)
                s = s[:index] + s[index + 1:]
                result += elem_one
            temp = s
        return result

print(Solution.sortString(0,"aaaabbbbcccc"))
print(Solution.sortString(0,"rat"))
print(Solution.sortString(0,"leetcode"))
print(Solution.sortString(0,"ggggggg"))
print(Solution.sortString(0,"gtqxozxzrssrzxzoxqtg"))