class Solution(object):
    def uniqueMorseRepresentations(self, words):

        Morse_alphabet =dict( a =".-", b ="-...", c = "-.-.",d = "-..",e = ".", f = "..-.", g =  "--.", h = "....", i = "..", j = ".---", k =  "-.-", l = ".-..", m = "--", n = "-.", o = "---",
        p = ".--.", q = "--.-", r = ".-.", s = "...", t = "-", u = "..-", v = "...-", w = ".--", x = "-..-", y = "-.--", z = "--..")

        result = []
        for word in words:
            morse_word = ""
            for i in range(0,len(word)):
                morse_word += Morse_alphabet.get(word[i])
            result.append(morse_word)

        result = set(result)

        return len(result)

print(Solution.uniqueMorseRepresentations(0,["gin", "zen", "gig", "msg"]))