class Solution(object):
    def countCharacters(self, words, chars):

        temp = []

        for word in words:

            for char in word:
                fl = True
                if word.count(char) > chars.count(char):
                    fl = False
                    break

            if fl:
                    temp.append(word)

        result = 0
        for i in range(0, len(temp)):
            result += len(temp[i])

        return result


print(Solution.countCharacters(0,["cat","bt","hat","tree"], "atach"))
print(Solution.countCharacters(0,["hello","world","leetcode"],"welldonehoneyr"))
