class Solution(object):
    def findWords(self, words):

        Result = []
        for letter in words:
            n = 0
            m = 0
            k = 0
            for j in range(0,len(letter)):
                if letter[j] in "QWERTYUIOPqwertyuiop":
                    n += 1
                elif letter[j] in "ASDFGHJKLasdfghjkl":
                    m += 1
                elif letter[j] in "ZXCVBNMzxcvbnm":
                    k += 1
                if n == len(letter) or m == len(letter) or k == len(letter):
                    Result.append(letter)

        return Result


print(Solution.findWords(0,["Hello", "Alaska", "Dad", "Peace"]))