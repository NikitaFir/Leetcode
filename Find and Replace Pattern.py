class Solution(object):
    def transform(self, word):

        i = 0
        k = 1
        while i != len(word):
            if word[i].isalpha():
                word = word.replace(word[i], str(k))
                k += 1
            i += 1
        return word

    def findAndReplacePattern(self, words, pattern):

        result = []
        pattern = Solution.transform(self,pattern)

        for word in words:
            k = Solution.transform(self,word)
            if pattern == k:
                result.append(word)
        return result

print(Solution.findAndReplacePattern(0,["abc","deq","mee","aqq","dkd","ccc"],"abb"))