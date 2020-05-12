class Solution(object):
    def toGoatLatin(self, S):

        words = S.split(' ')

        vowel = set(['a', 'e', 'i', 'o', 'u'])

        result = []
        k = 0
        for word in words:
            k += 1
            if word[0].lower() in vowel:
                temp = word + "ma" + ("a" * k)
                result.append(temp)
            else:
                temp = word[1:] + word[:1] + "ma" + ("a" * k)
                result.append(temp)

        goat_said =' '.join(result)

        return goat_said

print(Solution.toGoatLatin(0,"I speak Goat Latin"))