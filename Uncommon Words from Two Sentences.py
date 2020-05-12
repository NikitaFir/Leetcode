class Solution(object):
    def uncommonFromSentences(self, A, B):

        k1 = A.split(' ')
        k2 = B.split(' ')
        l1 =set(k1)
        l2 = set(k2)

        temp = list(l1.union(l2) - l1.intersection(l2))
        result = []
        for word in temp:
            if k1.count(word) <= 1 and k2.count(word) <= 1:
                result.append(word)
        return result

print(Solution.uncommonFromSentences(0,"this apple is sweet","this apple is sour"))
print(Solution.uncommonFromSentences(0,"apple apple", "banana"))