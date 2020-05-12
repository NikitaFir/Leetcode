class Solution(object):
    def mostCommonWord(self, paragraph, banned):

        paragraph = paragraph.replace("'", " ")
        paragraph = paragraph.replace(",", " ")
        paragraph = paragraph.replace(";", " ")
        paragraph = paragraph.replace(".", " ")
        paragraph = paragraph.replace("?", " ")
        paragraph = paragraph.replace("!", " ")
        words = paragraph.lower().split(" ")

        noDup = set(words)
        max_ = 0
        for word in noDup:
            if words.count(word) > max_ and word not in banned and word != "" :
                max_ = words.count(word)
                result = word

        return result

print(Solution.mostCommonWord(0,"Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))

